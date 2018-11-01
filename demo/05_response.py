from flask import Flask, request, abort, Response, make_response


app = Flask(__name__)


@app.route("/index")
def index():
    # 1 使用元组 返回自定义的响应信息
    # 响应体  状态码 响应头
    # return "index page", 200, [("Itcast", "python"), ("City", "shanghai")]

    # 2 使用make_response构造 响应信息
    rep = make_response("index page2")
    rep.status = "999 itcast"  # 设置状态码
    rep.headers["city"] = "shanghai"
    return rep


if __name__ == '__main__':
    app.run(debug=True)
