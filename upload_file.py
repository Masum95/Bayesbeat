import requests


files = {'file': open('sample.pdf', 'rb')}
values = {'device_id': 'd_1234', 'recorded_at':'11/12/2020'}

url = 'http://127.0.0.1:8000/file/upload/'
response = requests.post(url, files=files, data=values)

print(response)
