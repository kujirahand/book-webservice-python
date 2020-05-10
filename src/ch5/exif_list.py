from PIL import Image
import PIL.ExifTags as ExifTags

# 画像ファイルを読み込む --- (*1)
img = Image.open('test.jpg')
# Exif情報を得る --- (*2)
exif = img._getexif()
# Exif情報を列挙する --- (*3)
for id, value in exif.items():
    tag = ExifTags.TAGS[id]
    print(tag + ":", value)

