# テスト用の郵便番号
code = '1510065'

# データベースに接続
import sqlite3
conn = sqlite3.connect('zip.sqlite')

# 郵便番号を検索
c = conn.cursor()
res = c.execute('SELECT * FROM zip WHERE code=?', [code])
for row in res:
    print(row)
