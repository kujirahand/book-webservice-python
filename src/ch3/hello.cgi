#!/usr/local/bin/python3.7
#!/usr/local/bin/python3.4
##########################
# [注意点1]
# (1) Pythonのバージョンを確認して、このファイルの1行目を変更
# (2) パーミッションを指定のものに変更
#
# ロリポップであれば以下のURLを確認してください。
#   契約時期やプランによってPythonバージョンが異なります。
# [URL] https://lolipop.jp/manual/hp/cgi/
#
# [注意点2]
# 改行コードはLFのまま変更しないようにしてください。
#
# [ヒント]
# もし、SSHで接続可能なら、SSHでサーバに接続して
# 以下のコマンドが実行可能か確認してください。
# $ ./hello.cgi


# Content-Typeのヘッダを出力 --- (*1)
print("Content-Type: text/html; charset=UTF-8")
print("")

# メッセージを出力 --- (*2)
print("Hello, World!")

