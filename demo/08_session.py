from flask import Flask, session

app = Flask(__name__)

# 使用session需要配置SECRET_KEY
app.config['SECRET_KEY'] = "dhfjfjerfnsdn323j4j23nfd"

# flask默认把session保存到cookie中


@app.route("/login")
def login():
    # 设置session数据
    session['name'] = "python"

    return "login success"


@app.route("/index")
def index():
    # 获取session数据
    name = session.get("name")
    return "hello %s" % name


if __name__ == '__main__':
    app.run(debug = True)
