from flask import Flask, request, redirect
from tinydb import TinyDB
import qrcode

# アクセスをカウントした後にジャンプするURL --- (*1)
JUMP_URL = 'https://kujirahand.com/'
FILE_COUNTER = './counter.json'

# Flaskを生成 --- (*2)
app = Flask(__name__)
# TinyDBを開く --- (*3)
db = TinyDB(FILE_COUNTER)

@app.route('/')
def index():
    # 訪問用QRコードを生成 --- (*4)
    url = request.host_url + 'jump'
    img = qrcode.make(url)
    img.save('./static/qrcode_jump.png')
    # 画面にQRコードを表示 --- (*5)
    counter = get_counter()
    return '''
    <h1>以下のQRコードを名刺に印刷</h1>
    <img src="static/qrcode_jump.png" width=300><br>
    {0}<br>
    現在の訪問者は、{1}人です。
    '''.format(url, counter) 

@app.route('/jump')
def jump():
    # アクセスをカウントアップ --- (*6)
    v = get_counter()
    table = db.table('count_visitor')
    table.update({'v': v + 1})
    # 任意のURLにリダイレクト --- (*7)
    return redirect(JUMP_URL)

def get_counter():
    # アクセスを数える --- (*8)
    table = db.table('count_visitor')
    a = table.all()
    if len(a) == 0:
        # もし最初なら値0を挿入する --- (*9)
        table.insert({'v': 0})
        return 0
    return a[0]['v']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)


