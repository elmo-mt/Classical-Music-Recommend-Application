import os
from flask import Flask, request, render_template
from model2 import recommend  # model.pyからrecommend関数をインポート

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])  # トップページのルーティング
def top():
    return render_template("top.html")


@app.route("/kibun1", methods=["GET"])  # 気分入力ページのルーティング
def kibun1():
    return render_template("kibun1.html")


@app.route("/kibun2", methods=["GET", "POST"])  # 出力ページのルーティング
def kibun2():
    if request.method == "GET":
        return render_template(
            "kibun2.html",
            name=name,
            introduction_title=introduction_title,
            introduction_text=introduction_text,
            url=url,
        )
    elif request.method == "POST":
        favs = request.form.getlist("fav")  # name属性がfavのcheckboxから複数の値を取得
        data_str = ",".join(favs)
        name, introduction_title, introduction_text, url = recommend(data_str)
        return render_template(
            "kibun2.html",
            name=name,
            introduction_title=introduction_title,
            introduction_text=introduction_text,
            url=url,
        )  # 左辺がHTML、右辺がPython側の変数


@app.route("/introduction", methods=["GET", "POST"])  # 出力ページのルーティング
def introduction():
    if request.method == "GET":
        return render_template(
            "introduction.html",
            name=name,
            introduction_title=introduction_title,
            introduction_text=introduction_text,
        )
    elif request.method == "POST":
        favs = request.form.getlist("fav")  # name属性がfavのcheckboxから複数の値を取得
        data_str = ",".join(favs)
        name, introduction_title, introduction_text = recommend(data_str)
        return render_template(
            "introduction.html",
            name=name,
            introduction_title=introduction_title,
            introduction_text=introduction_text,
        )  # 左辺がHTML、右辺がPython側の変数


if __name__ == "__main__":
    app.run(debug=True)
