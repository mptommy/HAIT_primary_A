from flask import Flask, render_template, request, make_response, jsonify
from flask_bootstrap import Bootstrap
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
        # アップロードされたファイルを受け取って保存する
        paths = []

        if request.files.getlist('upload_files')[0].filename:

            upload_files = request.files.getlist('upload_files')

            if len(upload_files)!=2:
                return make_response(jsonify({'result':'expected 2 images but got more or less images.'}))


            for upload_file in upload_files:
                #受信したファイルを保存
                path = "./static/request/" + datetime.now().strftime("%Y%m%d%H%M%S") + ".png"
                upload_file.save(path)
                paths.append(path)

        else:
            return make_response(jsonify({'result':'file upload error'}))
        
        
        
        
        #各自作関数による処理
        _, maskimage = gazou.detect_red_color(paths[0], paths[1])
        red_path =  "./static/red_masked/" + datetime.now().strftime("%Y%m%d%H%M%S") + ".png"
        cv2.imwrite(red_path, maskimage)

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
    alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
    return render_template('result.html',dic=dicc, alphabets = alphabets)


if __name__ == "__main__":
    app.run(debug=True)