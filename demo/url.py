from flask import Flask, redirect, url_for

# 创建flask的应用对象
# __name__表示当前的模块名字
#                   模块名, flask以这个模块所在的这个模块所在的目录为总目录,默认这个目录中的static为静态目录, templates为模板目录
app = Flask(__name__)

app.config.from_pyfile("config.cfg")


# 通过route来进行视图函数和路由的映射
@app.route("/")
def index():
    """ 定义的视图函数 """
    return "Hello, Flask"


# 通过methods限定访问方式
@app.route("/post_only", methods=["GET", "POST"])
def post_only():
    return "post only page"


@app.route("/hello", methods=["POST"])
def hello():
    return "hello 1"


@app.route("/hello", methods=["GET"])
def hello2():
    return "hello 2"


@app.route("/login")
def login():
    # 使用url_for函数,通过视图名来找到视图对应的url路由
    url = url_for("index")
    return redirect(url)


if __name__ == '__main__':

    # 通过url_map可以查看整个flask中的路由信息
    print(app.url_map)
    # 设置参数启动flask
    app.run(debug=True)
