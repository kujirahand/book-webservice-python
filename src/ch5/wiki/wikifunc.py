import os, markdown

# データ保存先ディレクトリ --- (*1)
DIR_DATA = os.path.dirname(__file__) + '/data'

# マークダウン変換用オブジェクト --- (*2)
md = markdown.Markdown(extensions=['tables'])

# Wikiページ名から実際のファイルパスへ変換 --- (*3)
def get_filename(page_name):
    return DIR_DATA + "/" + page_name + ".md"

# ファイルを読みHTMLに変換して返す --- (*4)
def read_file(page_name, html=False):
    path = get_filename(page_name)
    if os.path.exists(path):
        with open (path, "rt", encoding="utf-8") as f:
            s = f.read()
            if html: s = md.convert(s) # --- (*5)
            return s
    return ""

# ファイルへ書き込む --- (*6)
def write_file(page_name, body):
    path = get_filename(page_name)
    with open (path, "wt", encoding="utf-8") as f:
        f.write(body)

