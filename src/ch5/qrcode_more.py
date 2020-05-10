import qrcode

# QRコードの生成で細かい設定を行う場合 --- (*1)
qr = qrcode.QRCode(
    box_size=4,
    border=8,
    version=12,
    error_correction=qrcode.constants.ERROR_CORRECT_Q)
# 描画するデータを指定する --- (*2)
qr.add_data('https://kujirahand.com/')
# QRコードの元データを作る --- (*3)
qr.make()
# データをImageオブジェクトとして取得 --- (*4)
img = qr.make_image()
# Imageをファイルに保存 --- (*5)
img.save('qrcode2.png')
print('ok')

