from flask import Flask
from werkzeug.routing import BaseConverter


app = Flask(__name__)


# 转换器
# 127.0.0.1:5000/goods/123
# @app.route("/goods/<int:goods_id>")
@app.route("/goods/<goods_id>")  # 不加转换器类型,默认是普通字符串规则(除了/以外的任意字符)
def goods_detail(goods_id):
    return "goods detail page %d" % goods_id


# 自定义转换器步骤
# 1.定义自己的转换
class RegexConverter(BaseConverter):
    """自定义手机号转换器"""
    # url_map是固定参数
    def __init__(self, url_map, regex):
        # 调用父类的初始化方法
        super(RegexConverter, self).__init__(url_map)
        # 将正则表达式的参数保存到对象属性中,flask会去使用这个属性阿里进行路由的正则匹配
        self.regex = regex


# 2.设置将自定义的转换器添加到flask应用中
app.url_map.converters['re'] = RegexConverter


# 3.使用转换器
@app.route("/send/<re(r'1[34578]\d{9}'):mobile>")
def send_msg(mobile):
    return "send msg to %s" % mobile


if __name__ == '__main__':
    app.run(debug=True)
