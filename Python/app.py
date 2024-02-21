# 모듈 import
from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

# MySQL 데이터베이스 연결
db = pymysql.connect(host='localhost', user='root', password='1234', db='flask', charset='utf8')


# 사용자 목록 확인 페이지
@app.route('/users')
def show_users_table():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM userInfo") # userInfo 테이블 렌더링
    users = cursor.fetchall()
    cursor.close()
    return render_template("users.html", users=users)


# 메인 페이지
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # POST 요청에서 userID와 userPW를 가져오기
        userID = request.form.get("ID")
        userPW = request.form.get("PW")

        # 서버 콘솔에 출력 테스트
        print(f"userID: {userID}")
        print(f"userPW: {userPW}")

        # 데이터베이스 커서 생성
        cursor = db.cursor()

        # SQL 쿼리 실행
        sql = "INSERT INTO userInfo (userID, userPW) VALUES (%s, %s)"
        cursor.execute(sql, (userID, userPW))

        # 데이터베이스에 적용
        db.commit()

        # 데이터베이스 커넥션 닫기
        cursor.close()

        return "POST 처리 성공"
    else:
        return render_template("index.html")


# 회원가입 페이지
@app.route('/signup')
def signup():
    return "회원가입 페이지"


# 비밀번호 찾기 페이지
@app.route('/forgot')
def forgot():
    return "비밀번호 찾기 페이지"


# 서버 실행
if __name__ == '__main__':
    app.run(debug=True)
