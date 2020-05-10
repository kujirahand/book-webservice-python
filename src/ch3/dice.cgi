#!/usr/local/bin/python3.4

# Content-Typeのヘッダを出力
print("Content-Type: text/html; charset=UTF-8")
print("")

# サイコロを表示
import random
dice = random.randint(1, 6)
# HTMLに埋め込んで表示
print("<html><body><h1>")
print("Dice =", dice)
print("</h1></body></html>")

