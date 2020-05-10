from flask import Flask, redirect
from flask import render_template, request
import wikifunc

# Flaskインスタンス生成
app = Flask(__name__)

# Wikiのメイン画面
@app.route('/')
def index():
    return show('FrontPage')

# 新規作成画面
@app.route('/new')
def new_page():
    page_name = request.args.get("page_name")
    if page_name is None:
      return render_template('new.html')
    else:
      return redirect('/edit/' + page_name)

# Wikiの編集画面 --- (*1)
@app.route('/edit/<page_name>')
def edit(page_name):
    body, hash = wikifunc.read_file(page_name)
    return render_template('edit.html',
      page_name=page_name,
      body=body,
      hash=hash,
      warn='')

# 編集内容を保存する --- (*2)
@app.route('/edit_save/<page_name>', methods=["POST"])
def edit_save(page_name):
    body2 = request.form.get("body")
    hash2 = request.form.get("hash")
    # 編集開始時点より別の編集があったか確認
    body1, hash1 = wikifunc.read_file(page_name)
    if hash1 != hash2: # 編集の競合があった
        # 差分を調査
        print("diff=", hash1, hash2)
        res = wikifunc.get_diff(page_name, body2, hash2)
        return render_template('edit.html',
            page_name=page_name,
            body=res,
            hash=hash1,
            warn='編集に競合がありました。')
    # 競合がなければ保存 --- (*3)
    wikifunc.write_file(page_name, body2)
    return redirect('/' + page_name)

# Wikiの表示
@app.route('/<page_name>')
def show(page_name):
    body, _ = wikifunc.read_file(page_name, html=True)
    return render_template('show.html',
      page_name=page_name,
      body=body)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

