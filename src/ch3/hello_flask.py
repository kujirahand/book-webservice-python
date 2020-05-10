from flask import Flask

# Flaskのインスタンスを作成 --- (*1)
app = Flask(__name__)

# ルーティングの指定 --- (*2)
@app.route('/')
def index():
    return "Hello, World!"

# 実行する --- (*3)
if __name__ == '__main__':
    app.run(host='0.0.0.0')

