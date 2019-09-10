import geocoder

if __name__ == '__main__':
    print('Oi')

    geo_result = geocoder.osm("Av liberdade. Lisboa. Portugal")
    print(geo_result.geojson)