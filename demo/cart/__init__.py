from flask import Blueprint

# 创建一个蓝图
app_cart = Blueprint("app_cart", __name__, template_folder="templates", static_folder="static")

# __init__文件被执行时，把视图加载进来，让蓝图与应用知道视图的存在
from .views import get_cart