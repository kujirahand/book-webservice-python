from tinydb import TinyDB, Query
import time, os

# パスの指定 --- (*1)
BASE_DIR = os.path.dirname(__file__)
DATA_FILE = BASE_DIR + '/data/data.json'

# データベースを開く --- (*2)
db = TinyDB(DATA_FILE)

# お気に入り登録用のfavテーブルのオブジェクトを返す --- (*3)
def get_fav_table():
    return db.table('fav'), Query()

def add_fav(id, fav_id): # --- (*4)
    table, q = get_fav_table()
    a = table.search(
        (q.id == id) & (q.fav_id == fav_id))
    if len(a) == 0:
        table.insert({'id': id, 'fav_id': fav_id})

def is_fav(id, fav_id): # --- (*5)
    table, q = get_fav_table()
    a = table.get(
        (q.id == id) & (q.fav_id == fav_id))
    return a is not None

def remove_fav(id, fav_id): # --- (*6)
    table, q = get_fav_table()
    table.remove(
        (q.id == id) & (q.fav_id == fav_id))

def get_fav_list(id): # --- (*7)
    table, q = get_fav_table()
    a = table.search(q.id == id)
    return [row['fav_id'] for row in a]

# 俳句保存用のtextテーブルのオブジェクトを返す --- (*8)
def get_text_table():
    return db.table('text'), Query()

def write_text(id, text): # --- (*9)
    table, q = get_text_table()
    table.insert({
        'id': id, 
        'text': text,
        'time': time.time()})

def get_text(id): # --- (*10)
    table, q = get_text_table()
    return table.search(q.id == id)

# タイムラインに表示するデータを取得する --- (*11)
def get_timelines(id):
    # お気に入りユーザーの一覧を取得 --- (*12)
    table, q = get_text_table()
    favs = get_fav_list(id)
    favs.append(id) # 自身も検索対象に入れる
    # 期間を指定して作品一覧を取得 --- (*13)
    tm = time.time() - (24*60*60) * 30 # 30日分
    a = table.search(
        q.id.one_of(favs) & (q.time > tm))
    return sorted(a,
            key=lambda v:v['time'],
            reverse=True) # --- (*14)

