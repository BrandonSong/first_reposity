from flask import Flask, request, abort, Response


app = Flask(__name__)


@app.route("/login", methods=["GET"])
def login():
    """登录视图"""
    name = ""
    pwd = ""
    if name != "mike" or pwd != "admin":
        # 使用abort函数可以立即终止视图函数的执行
        # 并可以返回给前端特定的信息
        # 方式1：传递状态码信息 必须是标准的http状态码
        abort(404)

        # 方式2：传递响应体信息，返回的信息必须是Response对象
        # resp = Response("login failed")
        # abort(resp)
    return "login"


@app.errorhandler(404)
def handle_404_error(error):
    """自定义处理404错误的方法"""
    # 这个函数的返回值会是前端用户看到的最终结果
    return "您访问的页面不见了,错误信息:%s" % error


if __name__ == '__main__':
    app.run(debug=True)