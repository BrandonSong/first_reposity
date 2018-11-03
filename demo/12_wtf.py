from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo


app = Flask(__name__)


# 定义表单的模型类
class RegisterForm(FlaskForm):
    """自定义的注册表单模型类"""
    # label 说明标签
    # validators 验证器(验证参数是否符合规则)
    # Datarequired 保证数据必须填写,并且不能为空
    user_name = StringField(label="用户名", validators=[DataRequired(message="用户名不能为空")])
    password = PasswordField(label="密码", validators=[DataRequired(message="密码不能为空")])
    password2 = PasswordField(label="确认密码", validators=[DataRequired("确认密码不能为空"),
                                                        EqualTo("password", message="密码不一致")])


@app.route("/index")
def index():
    return "index page"


@app.route("/register")
def register():
    form = RegisterForm()


if __name__ == '__main__':
    app.run(debug=True)