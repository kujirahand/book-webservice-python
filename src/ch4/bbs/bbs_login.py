from flask import session, redirect

# ログイン用ユーザーの一覧を定義 --- (*1)
USERLIST = {
    'taro': 'aaa',
    'jiro': 'bbb',
    'sabu': 'ccc',
}

# ログインしているか調べる --- (*2)
def is_login():
    return 'login' in session

# ログイン処理 --- (*3)
def try_login(user, password):
    # 該当ユーザーがいるか？
    if user not in USERLIST: return False
    # パスワードが合っているか？
    if USERLIST[user] != password: return False
    # ログイン処理 --- (*4)
    session['login'] = user
    return True

# ログアウト処理 --- (*5)
def try_logout():
    session.pop('login', None)
    return True

# セッションからユーザー名を得る --- (*6)
def get_user():
    if is_login(): return session['login']
    return 'not login'
