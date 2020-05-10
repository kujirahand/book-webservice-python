import exif_gps
import geocoder

# 写真から位置情報を取得
lat, lng = exif_gps.get_gps('test.jpg')
if lat is None:
  print('位置情報はありません。')
  quit()

# 逆ジオコーディング(OpenStreetMap APIを利用)
g = geocoder.osm((lat, lng), method='reverse')
print('写真の住所:')
print(g.address)

