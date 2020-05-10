from tinydb import TinyDB, where
import uuid, time, os

# パスの指定 --- (*1)
BASE_DIR = os.path.dirname(__file__)
FILES_DIR = BASE_DIR + '/files'
DATA_FILE = BASE_DIR + '/data/data.json'

# アップロードされたファイルとメタ情報の保存
def save_file(upfile, meta):
    # UUIDの生成 --- (*2)
    id = 'FS_' + uuid.uuid4().hex
    # アップロードされたファイルを保存 --- (*3)
    upfile.save(FILES_DIR + '/' + id)
    # メタデータをDBに保存 --- (*4)
    db = TinyDB(DATA_FILE)
    meta['id'] = id
    # 期限を計算 --- (*5)
    term = meta['limit'] * 60 * 60 * 24
    meta['time_limit'] = time.time() + term
    # 情報をデータベースに挿入 --- (*6)
    db.insert(meta)
    return id

# データベースから任意のIDのデータを取り出す --- (*7)
def get_data(id):
    db = TinyDB(DATA_FILE)
    f = db.get(where('id') == id)
    if f is not None:
        f['path'] = FILES_DIR + '/' + id
    return f

# データを更新する --- (*8)
def set_data(id, meta):
    db = TinyDB(DATA_FILE)
    db.update(meta, where('id') == id)

# 全てのデータを取得する --- (*9)
def get_all():
    db = TinyDB(DATA_FILE)
    return db.all()

# アップロードされたファイルとメタ情報の削除 --- (*10)
def remove_data(id):
    # ファイルを削除 --- (*11)
    path = FILES_DIR + '/' + id
    os.remove(path)
    # メタデータを削除 --- (*12)
    db = TinyDB(DATA_FILE)
    db.remove(where('id') == id)
