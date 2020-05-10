import re, sqlite3, photo_file

# データベースを開く --- (*1)
def open_db():
    conn = sqlite3.connect(photo_file.DATA_FILE)
    conn.row_factory = dict_factory
    return conn

# SELECT句の結果を辞書型で得られるようにする --- (*2)
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# SQLを実行する --- (*3)
def exec(sql, *args):
    db = open_db()
    c = db.cursor()
    c.execute(sql, args)
    db.commit()
    return c.lastrowid

# SQLを実行して結果を得る --- (*4)
def select(sql, *args):
    db = open_db()
    c = db.cursor()
    c.execute(sql, args)
    return c.fetchall()

