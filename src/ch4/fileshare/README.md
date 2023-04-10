# ファイル転送サービス

(注意) Flaskはバージョン1.1.1をご利用ください。

```
pip install Flask==1.1.1
```

2022年のFlask 2.0でパラメータ名に仕様変更がありました。

そのため、[こちら](https://github.com/pallets/flask/issues/4753)にあるように、send_fileを使う時、`attachment_filename`を`download_name`と変更してください。

