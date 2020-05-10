from flask import Flask, request 
import math
# 1ページに表示するデータ数
limit = 3
# サンプルデータ --- (*1)
data = [
    {"name": "リンゴ", "price": 370},
    {"name": "イチゴ", "price": 660},
    {"name": "バナナ", "price": 180},
    {"name": "マンゴ", "price": 450},
    {"name": "トマト", "price": 250},
    {"name": "セロリ", "price": 180},
    {"name": "パセリ", "price": 220},
    {"name": "ミカン", "price": 530},
    {"name": "エノキ", "price": 340}]

app = Flask(__name__)

# ブラウザのメイン画面 --- (*2)
@app.route('/')
def index():
    # ページ番号を得る --- (*3)
    page_s = request.args.get('page', '0')
    page = int(page_s)
    # 表示データの先頭を計算 --- (*4)
    index = page * limit
    # 表示データを取り出す --- (*5)
    s = '<div>'
    for i in data[index : index+limit]:
        s += '<div class="item">'
        s += '品名: ' + i['name'] + '<br>'
        s += '値段: ' + str(i['price']) + '円'
        s += '</div>'
    s += '</div>'
    # ページャーを作る --- (*6)
    s += make_pager(page, len(data), limit)
    return '''
    <html><meta charset="utf-8">
    <meta name="viewport"
       content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="static/pure-min.css">
    <style> .item { border: 1px solid silver;
                    background-color: #f0f0ff;
                    padding: 9px; margin: 15px; } </style>
    <body><h1 style="text-align:center;">商品</h1>
    ''' + s + '</body></html>'

def make_button(href, label):
    klass = 'pure-button'
    if href == '#': klass += ' pure-button-disabled'
    return '''
    <a href="{0}" class="{1}">{2}</a>
    '''.format(href, klass, label)

def make_pager(page, total, per_page):
    # ページ数を計算 --- (*7)
    page_count = math.ceil(total / per_page)
    s = '<div style="text-align:center;">'
    # 前へボタン --- (*8)
    prev_link = '?page=' + str(page - 1)
    if page <= 0: prev_link = '#'
    s += make_button(prev_link, '←前へ')
    # ページ番号 --- (*9)
    s += '{0}/{1}'.format(page+1, page_count)
    # 次へボタン --- (*10)
    next_link = '?page=' + str(page + 1)
    if page >= page_count - 1: next_link = '#'
    s += make_button(next_link, '次へ→')
    s += '</div>'
    return s

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


