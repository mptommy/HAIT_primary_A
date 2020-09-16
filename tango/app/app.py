from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from PIL import Image
import cv2
from datetime import datetime

import gsoperate
import gazou
import diction
import gocr

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        # アップロードされたファイルを受け取って保存してPILImageで読み込む
        f = request.files["file"]
        filepath = "./static/request/" + datetime.now().strftime("%Y%m%d%H%M%S") + ".png"
        f.save(filepath)
        image = Image.open(filepath)
        
        
        #各自作関数による処理
        _, mimage = gazou.detect_red_color(image)
        red_path =  "./static/red_masked/" + datetime.now().strftime("%Y%m%d%H%M%S") + ".png"
        cv2.imwrite(red_path, mimage)

        words = gocr.text_detection(red_path)

        dic = diction.transdict(words)

        gsoperate.gsupdate(dic)
        
        message = '単語帳を更新しました'

        
        return render_template("index.html", message=message)

# 単語テスト
@app.route('/result')
def test():
    #スプレッドシートから単語データを読み込む
    dicc = gsoperate.gsread()
    
    return render_template('result.html',dic=dicc)


if __name__ == "__main__":
    app.run(debug=True)