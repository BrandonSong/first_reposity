from flask import Flask, make_response, request


app = Flask(__name__)


@app.route("/set_cookies")
def set_cookies():
    resp = make_response("success")
    # 默认有效期是临时有效 浏览器关闭就失效
    # resp.set_cookie("itcast", "python")

    # 设置有效期 单位秒
    resp.set_cookie("itcast1", "python1", max_age=3600)
    return resp


# 获取cookie
@app.route("/get_cookies")
def get_cookies():
    c1 = request.cookies.get("itcast")
    return c1


# 删除cookie
@app.route("/delete_cookie")
def delete_cookie():
    resp = make_response("del success")
    resp.delete_cookies("itcast1")


if __name__ == '__main__':
    app.run(debug=True)
