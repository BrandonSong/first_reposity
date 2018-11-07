from flask import Flask, render_template, request, redirect, url_for
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


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == "GET":
        return render_template("register.html", form=form)
    else:
        # 判断form中的数据是否合理
        # 如果form中的数据完全满足所有的验证器,则返回真,否则返回假
        if form.validate_on_submit():
            # 提取数据
            user_name = form.user_name.data
            password = form.password.data
            password2 = form.password2.data
        else:
            render_template("register.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)