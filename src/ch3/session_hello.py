from flask import Flask, request, session, redirect
app = Flask(__name__)
app.secret_key = '9KStWezC' # 適当な値を設定 --- (*1)

@app.route('/')
def index():
    # ユーザー名の入力フォームを出力 --- (*2)
    return """
    <html><body><h1>ユーザー名を入力</h1>
    <form action="/setname" method="GET">
      名前: <input type="text" name="username">
      <input type="submit" value="開始">
    </form></body></html>
    """

@app.route('/setname')
def setname():
    # GETの値を取得 --- (*3)
    name = request.args.get('username')
    if name is None: return redirect('/')
    # セッションに値を保存 --- (*4)
    session['name'] = name
    # 他のページにリダイレクト --- (*5)
    return redirect('/morning')

def getLinks():
    return """
    <ul><li><a href="/morning">朝の挨拶</a></li>
    <li><a href="/hello">昼の挨拶</a></li>
    <li><a href="/night">夜の挨拶</a></li></ul>
    """

@app.route('/morning')
def morning():
    # セッションにnameがある？ --- (*6)
    if not ('name' in session):
        # nameがないのでルートに飛ばす --- (*7)
        return redirect('/')
    # セッションからユーザー名を得る --- (*8)
    name = session['name']
    return """
    <h1>{0}さん、おはようございます！</h1>{1}
    """.format(name, getLinks())

@app.route('/hello')
def hello():
    if not ('name' in session):
        return redirect('/')
    # セッションから名前を得てメッセージ出力 --- (*9)
    return """<h1>{0}さん、こんにちは！</h1>{1}
    """.format(session['name'], getLinks())

@app.route('/night')
def night():
    if not ('name' in session):
        return redirect('/')
    # セッションから名前を得てメッセージ出力 --- (*10)
    return """<h1>{0}さん、こんばんは！</h1>{1}
    """.format(session['name'], getLinks())

if __name__ == '__main__':
    app.run(host='0.0.0.0')

