from flask import Flask, render_template, request  #, redirect, url_for, abort
from PIL import Image
from datetime import datetime

import gsoperate

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
        image = mask_gazou(image)
        words = detect(image)
        dic = translate(words)
        gsoperate.gsupdate(dic)
        '''
        #スプレッドシートから単語データを引っ張る
        dicc = gsoperate.gsread()

        
        return render_template("index.html", dicc = dicc)


if __name__ == "__main__":
    app.run(debug=True)