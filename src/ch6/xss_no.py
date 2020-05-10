from flask import Flask, request 

app = Flask(__name__)

@app.route('/')
def index():
    # 入力フォームを表示
    return '''
    <html><meta charset="utf-8"><body>
    <form action="/kakunin" method="get">
    名前: <input name="name">
    <input type="submit" value="送信">
    </form></body></html>
    '''

@app.route('/kakunin')
def kakunin():
    import html
    # フォームの値を取得
    name = request.args.get('name', '')
    # エスケープ処理を施す
    name_html = html.escape(name) 
    # フォームに name を埋め込んで表示
    return '''
    <html><meta charset="utf-8"><body>
    <h1>名前は、{0}さんです。</h1>
    </body></html>
    '''.format(name_html)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
