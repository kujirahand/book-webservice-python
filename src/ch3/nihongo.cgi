#!/usr/local/bin/python3.4

# 日本語を表示するために必要
import sys
sys.stdin = open(sys.stdin.fileno(),  'r',
               encoding='UTF-8')
sys.stdout = open(sys.stdout.fileno(), 'w',
               encoding='UTF-8')
sys.stderr = open(sys.stderr.fileno(), 'w',
               encoding='UTF-8')

# Content-Typeのヘッダを出力
print("Content-Type: text/html; charset=UTF-8")
print("")

# 日本語を表示
print("<html><body><h1>")
print("賢い子は父親を喜ばせ，愚かな子は母親を悲しませる。")
print("</h1></body></html>")

