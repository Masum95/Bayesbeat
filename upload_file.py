import requests


# files = {'file': open('sample.pdf', 'rb')}
files = {'file': open('uncle_March.csv', 'rb')}

values = {'device_id': 'd_1234', 'timestamp':'1606507099'}


# url = 'https://bayesbeat.herokuapp.com/file/upload/'
url = 'http://127.0.0.1:8000/file/upload/'

response = requests.post(url, files=files, data=values)
files = {'file': open('uncle_March4.csv', 'rb')}

values = {'device_id': 'd_1234', 'timestamp':'1606507099'}
response = requests.post(url, files=files, data=values)

print(response)
