import os

# スクリプトのファイルパス
print("script path:", __file__)
# スクリプトを配置しているディレクトリのパス
print("script dir: ", os.path.dirname(__file__))

# スクリプトの絶対パス
apath = os.path.abspath(__file__)
print("script path abs:", apath)
print("script dir abs:", os.path.dirname(apath))

