from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

pymysql.install_as_MySQLdb()


app = Flask(__name__)


class Config(object):
    """配置参数"""
    # sqlAlchemy的配置参数
    SQLALCHEMY_DATABASE_URI = "mysql://root:1234@127.0.0.1:3306/author_book?charset=utf8"
    # 设置sqlalchemy自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SECRET_KEY = "jjfajffewoirjf3125jfkdn"


app.config.from_object(Config)


db = SQLAlchemy(app)


class Author(db.Model):
    """作者表"""
    __tablename__ = "tbl_authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)

    books = db.relationship("Book", backref="author")


class Book(db.Model):
    """图书表"""
    __tablename___ = "tbl_books"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey("tbl_authors.id"))


# 表单模型类
class AuthorBookForm(FlaskForm):
    """作者书籍表单类"""
    author_name = StringField(label="作者", validators=[DataRequired("作者名必填")])
    book_name = StringField(label="书籍", validators=[DataRequired("书籍名必填")])
    submit = SubmitField(label="保存")


@app.route("/")
def index():
    # 创建表单对象
    form = AuthorBookForm()

    if form.validate_on_submit():
        # 验证成功
        author_name = form.author_name.data
        book_name = form.book_name.data

        # 保存数据
        Author(name=author_name)

    # 查询数据库
    authors = Author.query.all()  # 作者列表
    return render_template("authors_book.html", authors=authors, form=form)


if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    #
    # au_xi = Author(name="我吃西红柿")
    # au_qian = Author(name="萧潜")
    # au_san = Author(name="唐家三少")
    #
    # db.session.add_all([au_qian, au_san, au_xi])
    # db.session.commit()
    #
    # bk_xi = Book(name="吞噬星空", author_id=au_xi.id)
    # bk_xi2 = Book(name="寸芒", author_id=au_qian.id)
    # bk_qian = Book(name="缥缈之旅", author_id=au_qian.id)
    # bk_san = Book(name="冰火魔厨", author_id=au_san.id)
    #
    # db.session.add_all([bk_qian, bk_san, bk_xi, bk_xi2])
    # db.session.commit()
    app.run(debug=True)




