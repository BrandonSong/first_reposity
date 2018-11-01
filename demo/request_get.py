from flask import Flask

# 创建flask的应用对象
# __name__表示当前的模块名字
#                   模块名, flask以这个模块所在的这个模块所在的目录为总目录,默认这个目录中的static为静态目录, templates为模板目录
app = Flask(__name__)

app.config.from_pyfile("config.cfg")


# 通过route来进行视图函数和路由的映射
@app.route("/")
def index():
    """ 定义的视图函数 """
    print(app.config.get("DEBUG"))
    return "Hello, Flask"


if __name__ == '__main__':
    # 启动flask程序
    # app.run()

    # 设置参数启动flask
    app.run(host="127.0.0.1", port=8080)
