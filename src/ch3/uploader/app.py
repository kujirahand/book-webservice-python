from flask import Flask, request, redirect
from datetime import datetime
import os

# 保存先のディレクトリとURLの指定 --- (*1)
IMAGES_DIR = './static/images'
IMAGES_URL = '/static/images'
app = Flask(__name__)

@app.route('/')
def index_page():
    # アップロードフォーム --- (*2)
    return """
    <html><body><h1>アップロード</h1>
    <form action="/upload"
          method="POST"
          enctype="multipart/form-data">
        <input type="file" name="upfile">
        <input type="submit" value="アップロード">
    </form>
    </body></html>
    """

@app.route('/upload', methods=['POST'])
def upload():
    # アップされていなければトップへ飛ばす --- (*3)
    if not ('upfile' in request.files):
        return redirect('/')
    # アップしたファイルのオブジェクトを得る --- (*4)
    temp_file = request.files['upfile']
    # JPEGファイル以外は却下する --- (*5)
    if temp_file.filename == '':
        return redirect('/')
    if not is_jpegfile(temp_file.stream):
        return '<h1>JPEG以外アップできません</h1>'
    # 保存先のファイル名を決める --- (*6)
    time_s = datetime.now().strftime('%Y%m%d%H%M%S')
    fname = time_s + '.jpeg'
    # 一時ファイルを保存先ディレクトリへ保存 --- (*7)
    temp_file.save(IMAGES_DIR + '/' + fname)
    # 画像の表示ページへ飛ぶ
    return redirect('/photo/' + fname)

@app.route('/photo/<fname>')
def photo_page(fname):
    # 画像ファイルがあるか確認する --- (*8)
    if fname is None: return redirect('/')
    image_path = IMAGES_DIR + '/' + fname
    image_url  = IMAGES_URL + '/' + fname
    if not os.path.exists(image_path):
        return '<h1>画像がありません</h1>'
    # 画像を表示するHTMLを出力する --- (*9)
    return """
    <h1>画像がアップロードされています</h1>
    <p>URL: {0}<br>File: {1}</p>
    <img src="{0}" width="400">
    """.format(image_url, image_path)

# JPEGファイルかどうかを確認する --- (*10)
def is_jpegfile(fp):
    byte = fp.read(2) # 先頭2バイトを読む
    fp.seek(0) # ポインタを先頭に戻す
    return byte[:2] == b'\xFF\xD8'

if __name__ == '__main__':
    app.run(host='0.0.0.0')

