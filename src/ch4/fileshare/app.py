from flask import Flask, redirect, request
from flask import render_template, send_file
import os, json, time
import fs_data # ファイルやデータを管理するモジュール --- (*1)

app = Flask(__name__)
MASTER_PW = 'abcd' # 管理用パスワード --- (*2)

@app.route('/')
def index():
    # ファイルのアップロードフォームを表示 --- (*3)
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # アップロードしたファイルのオブジェクト --- (*4)
    upfile = request.files.get('upfile', None)
    if upfile is None: return msg('アップロード失敗')
    if upfile.filename == '': return msg('アップロード失敗')
    # メタ情報を取得 --- (*5)
    meta = {
        'name': request.form.get('name', '名無し'),
        'memo': request.form.get('memo', 'なし'),
        'pw':   request.form.get('pw', ''),
        'limit': int(request.form.get('limit', '1')),
        'count': int(request.form.get('count', '0')),
        'filename': upfile.filename
    }
    if (meta['limit'] == 0) or (meta['pw'] == ''):
        return msg('パラメータが不正です。')
    # ファイルを保存 --- (*6)
    fs_data.save_file(upfile, meta)
    # ダウンロード先の表示 --- (*7)
    return render_template('info.html',
            meta=meta, mode='upload',
            url=request.host_url + 'download/' + meta['id'])

@app.route('/download/<id>')
def download(id):
    # URLが正しいか判定 --- (*8)
    meta = fs_data.get_data(id)
    if meta is None: return msg('パラメータが不正です')
    # ダウンロードページを表示 --- (*9)
    return render_template('info.html',
            meta=meta, mode='download',
            url=request.host_url + 'download_go/' + id)

@app.route('/download_go/<id>', methods=['POST'])
def download_go(id):
    # URLが正しいか再び判定 --- (*10)
    meta = fs_data.get_data(id)
    if meta is None: return msg('パラメータが不正です')
    # パスワードの確認 --- (*11)
    pw = request.form.get('pw', '')
    if pw != meta['pw']: return msg('パスワードが違います')
    # ダウンロード回数の確認 --- (*12)
    meta['count'] = meta['count'] - 1
    if meta['count'] < 0:
        return msg('ダウンロード回数を超えました。')
    fs_data.set_data(id, meta)
    # ダウンロード期限の確認 --- (*13)
    if meta['time_limit'] < time.time():
        return msg('ダウンロードの期限が過ぎています')
    # ダウンロードできるようにファイルを送信 --- (*14)
    return send_file(meta['path'],
            as_attachment=True,
            attachment_filename=meta['filename'])

@app.route('/admin/list')
def admin_list():
    # マスターパスワードの確認 --- (*15)
    if request.args.get('pw', '') != MASTER_PW:
        return msg('マスターパスワードが違います')
    # 全データをデータベースから取り出して表示 --- (*16)
    return render_template('admin_list.html', 
        files=fs_data.get_all(), pw=MASTER_PW)

@app.route('/admin/remove/<id>')
def admin_remove(id):
    # マスターパスワードを確認してファイルとデータを削除 --- (*17)
    if request.args.get('pw', '') != MASTER_PW:
        return msg('マスターパスワードが違います')
    fs_data.remove_data(id)
    return msg('削除しました')

def msg(s): # テンプレートを使ってエラー画面を表示
    return render_template('error.html', message=s)

# 日時フォーマットを簡易表示するフィルタ設定 --- (*18)
def filter_datetime(tm):
    return time.strftime(
            '%Y/%m/%d %H:%M:%S',
            time.localtime(tm))
# フィルタをテンプレートエンジンに登録
app.jinja_env.filters['datetime'] = filter_datetime

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

