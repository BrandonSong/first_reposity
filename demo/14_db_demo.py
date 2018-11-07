from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()


app = Flask(__name__)


class Config(object):
    """配置参数"""
    # sqlAlchemy的配置参数
    SQLALCHEMY_DATABASE_URI = "mysql://root:1234@127.0.0.1:3306/mytest"
    # 设置sqlalchemy自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True


app.config.from_object(Config)

# 创建数据库sqlAlchemy工具
db = SQLAlchemy(app)


# 创建数据库模型类(继承Model类)
# 表命的常见规范
# 1.数据库名缩写_表名
# 2.tal_表名
class User(db.Model):
    """用户模型类"""
    __tablename__ = "tbl_users"  # 设置表名

    id = db.Column(db.Integer, primary_key=True)  # 需自己设置主键 整型的主键会默认设置为自增
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey("tbl_roles.id"))

    def __repr__(self):
        """自定义显示对象的时候的信息"""
        return "Role object: name=%s" % self.name


# 创建角色模型类
class Role(db.Model):
    """用户角色表"""
    __tablename__ = "tbl_roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)

    users = db.relationship("User", backref="role")

    def __repr__(self):
        """自定义显示对象的时候的信息"""
        return "Role object: name=%s" % self.name


@app.route("/index")
def index():
    return "index page"


if __name__ == '__main__':
    # 清除数据库中的所有数据
    # db.drop_all()
    #
    # # 创建所有的表
    # db.create_all()
    #
    # # 创建对象
    # role1 = Role(name="admin")
    # # session对象记录对象任务
    # db.session.add(role1)
    # # 提交任务到数据库中
    # db.session.commit()
    #
    # role2 = Role(name="stuff")
    # db.session.add(role2)
    # db.session.commit()
    #
    # us1 = User(name="wang", email="wang@163.com", password="123456", role_id=role1.id)
    # us2 = User(name="zhang", email="zhang@189.com", password="123456", role_id=role2.id)
    # us3 = User(name="chen", email="chen@126.com", password="123456", role_id=role2.id)
    # us4 = User(name="zhou", email="zhou@163.com", password="123456", role_id=role1.id)
    #
    # # 一次保存多条数据
    # db.session.add_all([us1, us2, us3, us4])
    # db.session.commit()

    # 查询所有
    # Role.query.all()
    # 查询单个
    # Role.query.first()
    # Role.query.get(2)

    # 条件查询
    User.query.filter_by(name="wang").all()