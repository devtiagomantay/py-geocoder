import geocoder
from pprint import pprint

if __name__ == '__main__':
    address = 'Av liberdade. Lisboa. Portugal'
    geo_result = geocoder.osm(address)
    pprint(geo_result.geojson)
