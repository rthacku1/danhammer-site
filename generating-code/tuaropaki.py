import json
import requests
import datetime
import time


def grabber(coords, begin, end):
    base_url = 'http://wolak.enviro-service.appspot.com/vegetation/poly/series'
    payload = dict(coords=coords, begin=begin, end=end)
    r = requests.get(base_url, params=payload)
    print r.text
    return r.json()

with open('paddocks.geojson') as f:
    data = json.load(f)

paddock = data['features'][37]


def paddock_process(paddock):
    coords = str(paddock['geometry']['coordinates'][0][0])

    dicts = []
    for year in range(2000, 2016):
        data = grabber(coords, '%s-01-01' % year, '%s-12-30' % year)
        dicts += data
        time.sleep(4)

    