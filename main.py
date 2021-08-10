import time

import geoip2.database
from flask import Flask
from flask import request

app = Flask(__name__)


class LocationBlob:

    def __init__(self, location, city, country):
        self.location = location
        self.city = city
        self.country = country

def fetch_location_details(ip):
    with geoip2.database.Reader(
            'geolite2-city/GeoLite2-City.mmdb') as reader:
        response = reader.city(ip)#'172.217.12.164'
        response.country
        return LocationBlob(response.location.__dict__, response.city.__dict__, response.country.__dict__).__dict__


@app.route('/get-location')
def fetch():
    print("Request Received")
    return fetch_location_details(request.args.get('ip', type=str))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=106)
