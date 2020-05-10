from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    # URLパラメータを取得 --- (*1)
    a = request.args.get('a')
    b = request.args.get('b')
    # パラメータが設定されているか確認 --- (*2)
    if (a is None) or (b is None):
        return "パラメータが足りません。"
    # パラメータを数値に変換して計算 --- (*3)
    c = int(a) * int(b)
    # 結果を出力 --- (*4)
    return "<h1>" + str(c) + "</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')


