import os, json, datetime

# 保存先のファイルを指定 --- (*1)
BASE_DIR = os.path.dirname(__file__)
SAVE_FILE = BASE_DIR + '/data/log.json'

# ログファイル(JSON形式)を読み出す --- (*2)
def load_data():
    if not os.path.exists(SAVE_FILE):
        return []
    with open(SAVE_FILE, 'rt', encoding='utf-8') as f:
        return json.load(f)

# ログファイルへ書き出す --- (*3)
def save_data(data_list):
    with open(SAVE_FILE, 'wt', encoding='utf-8') as f:
        json.dump(data_list, f)

# ログを追記保存 --- (*4)
def save_data_append(user, text):
    # レコードを用意
    tm = get_datetime_now()
    data = {'name': user, 'text': text, 'date': tm}
    # 先頭にレコードを追記して保存 --- (*5)
    data_list = load_data()
    data_list.insert(0, data)
    save_data(data_list)

# 日時を文字列で得る
def get_datetime_now():
    now = datetime.datetime.now()
    return "{0:%Y/%m/%d %H:%M}".format(now)

