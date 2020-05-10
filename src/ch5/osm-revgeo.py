import geocoder

# 緯度経度を指定
pos = (35.659025, 139.745025)
# OpenStreetMapを使って逆ジオコーディング
g = geocoder.osm(pos, method='reverse')

print('Country:', g.country)
print('State:', g.state)
print('City:', g.city)
print('Street:', g.street)

