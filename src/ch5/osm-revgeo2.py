import geocoder
import pprint

pos = (35.659025, 139.745025)
g = geocoder.osm(pos, method='reverse')
pprint.pprint(g.json)


