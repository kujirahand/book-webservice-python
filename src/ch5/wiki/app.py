from flask import Flask, redirect
from flask import render_template, request
import wikifunc

# Flaskインスタンス生成
app = Flask(__name__)

# Wikiのメイン画面 --- (*1)
@app.route('/')
def index():
    return show('FrontPage')

# 新規作成画面 --- (*2)
@app.route('/new')
def new_page():
    page_name = request.args.get("page_name")
    if page_name is None:
      return render_template('new.html')
    else:
      return redirect('/edit/' + page_name)

# Wikiの編集画面 --- (*3)
@app.route('/edit/<page_name>')
def edit(page_name):
    return render_template('edit.html',
      page_name=page_name,
      body=wikifunc.read_file(page_name))

# 編集内容を保存する --- (*4)
@app.route('/edit_save/<page_name>', methods=["POST"])
def edit_save(page_name):
    body = request.form.get("body")
    wikifunc.write_file(page_name, body)
    return redirect('/' + page_name)

# Wikiの表示 --- (*5)
@app.route('/<page_name>')
def show(page_name):
    print(page_name)
    return render_template('show.html',
      page_name=page_name,
      body=wikifunc.read_file(page_name, html=True))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

