from flask import Flask, render_template, request  #, redirect, url_for, abort
from PIL import Image
import cv2
from datetime import datetime

import gsoperate
import gazou
import diction

app = Flask(__name__)
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
        
        '''
        #各自作関数による処理
        _, mimage = gazou.detect_red_color(image)
        red_path =  "./static/red_masked/" + datetime.now().strftime("%Y%m%d%H%M%S") + ".png"
        cv2.imwrite(red_path, mimage)

        words = detecr(red_path)

        dic = diction.transdict(words)

        gsoperate.gsupdate(dic)
        '''
        #スプレッドシートから単語データを引っ張る
        dicc = gsoperate.gsread()

        
        return render_template("index.html", dicc = dicc)


if __name__ == "__main__":
    app.run(debug=True)