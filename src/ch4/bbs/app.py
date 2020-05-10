from flask import Flask, redirect, url_for, session
from flask import render_template, request
import os, json, datetime
import bbs_login # ログイン管理モジュール --- (*1)
import bbs_data  # データ入出力用モジュール --- (*2)

# Flaskインスタンスと暗号化キーの指定
app = Flask(__name__)
app.secret_key = 'U1sNMeUkZSuuX2Zn'

# 掲示板のメイン画面 --- (*3)
@app.route('/')
def index():
    # ログインが必要 --- (*4)
    if not bbs_login.is_login():
        return redirect('/login')
    # ログ一覧を表示 --- (*5)
    return render_template('index.html',
            user=bbs_login.get_user(),
            data=bbs_data.load_data())

# ログイン画面を表示 --- (*6)
@app.route('/login')
def login():
    return render_template('login.html')

# ログイン処理 --- (*7)
@app.route('/try_login', methods=['POST'])
def try_login():
    user = request.form.get('user', '')
    pw = request.form.get('pw', '')
    # ログインに成功したらルートページへ飛ぶ
    if bbs_login.try_login(user, pw):
        return redirect('/')
    # 失敗した時はメッセージを表示
    return show_msg('ログインに失敗しました')

# ログアウト処理 --- (*8)
@app.route('/logout')
def logout():
    bbs_login.try_logout()
    return show_msg('ログアウトしました')

# 書き込み処理 --- (*9)
@app.route('/write', methods=['POST'])
def write():
    # ログインが必要 --- (*10)
    if not bbs_login.is_login():
        return redirect('/login')
    # フォームのテキストを取得 --- (*11)
    ta = request.form.get('ta', '')
    if ta == '': return show_msg('書込が空でした。')
    # データに追記保存 --- (*12)
    bbs_data.save_data_append(
            user=bbs_login.get_user(),
            text=ta)
    return redirect('/')

# テンプレートを利用してメッセージを出力 --- (*13)
def show_msg(msg):
    return render_template('msg.html', msg=msg)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

