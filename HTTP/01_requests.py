import requests


url = 'https://ya.ru'
response = requests.get(url)
print(response)
print(response.headers)
print(response.text)
print(response.ok)
print(f'Request to {url}. Status code is {response.status_code}.')



