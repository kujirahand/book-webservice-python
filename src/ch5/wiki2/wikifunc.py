import os, hashlib, re, subprocess, markdown

# 定数の指定 --- (*1)
DIR_DATA = os.path.dirname(__file__) + '/data'
DIR_BACKUP = DIR_DATA + '/backup'
DIFF3 = 'diff3'

# マークダウン変換用オブジェクト
md = markdown.Markdown(extensions=['tables'])

# Wikiページ名から実際のファイルパスへ変換
def get_filename(page_name):
    return DIR_DATA + "/" + page_name + ".md"

# バックアップファイルの保存先のパスを取得 --- (*2)
def get_backup(page_name, hash):
    if not os.path.exists(DIR_BACKUP):
        os.makedirs(DIR_BACKUP)
    return DIR_BACKUP + '/' + page_name + "." + hash

# ファイルを読みHTMLに変換して返す --- (*3)
def read_file(page_name, html=False):
    text = read_f(get_filename(page_name))
    hash = get_hash(text)
    print("read:", hash)
    if html: text = md.convert(text)
    return text, hash

# ファイルへ書き込む --- (*4)
def write_file(page_name, body):
    body = re.sub(r'\r\n|\r|\n', "\n", body)
    # メインファイル
    write_f(get_filename(page_name), body)
    # バックアップファイルを書き込む
    hash = get_hash(body)
    write_f(get_backup(page_name, hash), body)

# 差分を求める --- (*5)
def get_diff(page_name, text, hash):
    newfile = DIR_DATA + '/__投稿__'
    write_f(newfile, text)
    orgfile = DIR_DATA + '/__編集前__'
    backupfile = get_backup(page_name, hash)
    write_f(orgfile, read_f(backupfile))
    curfile = DIR_DATA + '/__更新__'
    write_f(curfile, read_f(get_filename(page_name)))
    cp = subprocess.run([
        DIFF3, '-a', '-m', 
        newfile, orgfile, curfile],
        encoding='utf-8', stdout=subprocess.PIPE)
    print(cp)
    res = cp.stdout
    res = res.replace(DIR_DATA + '/', '')
    return res

# ファイルを読むだけ
def read_f(path):
    text = ""
    if os.path.exists(path):
        with open (path, "rt", encoding="utf-8") as f:
            text = f.read()
    return text

# ファイルを書くだけ
def write_f(path, text):
    with open (path, "wt", encoding="utf-8") as f:
        f.write(text)

# ハッシュ値を求める
def get_hash(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()
