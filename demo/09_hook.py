from flask import Flask, request


app = Flask(__name__)


@app.route("hello")
def hello():
    print("hello 被执行")
    return "hello page"


@app.route("/index")
def index():
    print("index 执行")
    a = 1 / 0
    print(a)
    return "index page"


@app.before_first_request
def handle_before_first_request():
    """第一次请求处理之前被执行"""
    print("handle_before_first_request")


@app.before_request
def handle_before_request():
    """在每次请求之都被执行"""
    print("handle_before_request")


@app.after_request
def handle_after_request(response):
    """在每次请求（视图函数处理）之后都被执行, 视图函数没有出现异常"""
    print("handle_after_request")
    return response


@app.teardown_request
def handle_before_request(response):
    """在每次请求之后都被执行 无论视图函数是否出现异常(调试模式不生效)"""
    print(request.path)
    print("handle_teardown_request")
    return response


if __name__ == '__main__':
    app.run(debug=True)

