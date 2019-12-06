import requests


# url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-01-01&endtime=2014-01-02'
url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
response = requests.get(url, headers={'Accept': 'application/json'}, params =
            {'format': 'geojson',
             'starttime': '2019-01-01',
              'endtime': '2019-02-01',
             'latitude': '51.51',
             'longitude': '0.12',
             'maxradiuskm': '2000'
             })
# print(response.text)  # string type
print(response.json())  # dict type

data = response.json()
print(data['type'])
print(data['features'][0]['properties']['place'])
print(data['features'][1]['properties']['place'])
