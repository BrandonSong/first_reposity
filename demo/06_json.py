from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/index")
def index():
    # json就是字符串
    data = {
        "name": "python",
        "age": 18
    }

    # json.dumps  将python的字典转换为json字符串
    # json.loads  将json字符串转换为字典
    # 方式1
    # json_str = json.dumps(data)
    # return json_str, 200, {"Content-Type": "application/json"}

    # 方式2
    # jsonify帮助转为json数据,并设置响应头 Content-Type:application/json
    # return jsonify(data)
    

if __name__ == '__main__':
    app.run(debug=True)
