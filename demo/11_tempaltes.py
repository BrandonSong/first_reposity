from flask import Flask, render_template


app = Flask(__name__)


@app.route("/index")
def index():
    data = {
        "name": "golang",
        "age": 23,
        "my_dict": {"city": "shanghai"},
        "my_list": [1, 2, 3, 4, 50],
        "my_int": 1
    }
    return render_template("index.html", **data)


# 自定义过滤器
# 方式一 直接定义函数
def list_step_2(li):
    """自定义的过滤器"""
    return li[::2]


# 注册过滤器
# 参数一是使用的 参数二是注册名
app.add_template_filter(list_step_2, "list2")


# 装饰器完成过滤器注册
# 参数为注册名
@app.template_filter("li3")
def list_step_3(li):
    """自定义的过滤器"""
    return li[::3]


if __name__ == '__main__':
    # 通过管理对象来启动flask
    app.run(debug=True)
