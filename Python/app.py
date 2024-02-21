# 모듈 import
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return "POST 처리 성공"
    else:
        return render_template('index.html')


@app.route('/signup')
def signup():
    return "회원가입 페이지"


@app.route('/forgot')
def forgot():
    return "비밀번호 찾기 페이지"


if __name__ == '__main__':
    app.run(debug=True)
