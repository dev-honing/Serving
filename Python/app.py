# 모듈 import
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # POST 요청에서 userID와 userPW를 가져오기
        userID = request.form.get("ID")
        userPW = request.form.get("PW")

        # 서버 콘솔에 출력 테스트
        print(f"userID: {userID}")
        print(f"userPW: {userPW}")

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
