from flask import Flask, request


app = Flask(__name__)


@app.route("/upload", methods=["POST"])
def upload():
    """文件上传视图"""
    pic_obj = request.files.get('pic')
    if pic_obj is None:
        # 表示没有发送文件
        return "未上传文件"

    # 将文件保存到本地
    # 1.创建一个文件
    with open("./demo.jpg", "wb") as f:
        # 2.向文件写入内容
        data = pic_obj.read()
        f.write(data)
        return "上传成功"


if __name__ == '__main__':
    app.run(debug=True)