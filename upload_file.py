import requests
# url = 'http://127.0.0.1:8000/file/upload/'
url = 'http://192.168.31.62:8000/file/upload/'
# url = 'https://bayesbeat.herokuapp.com/file/upload/'


files = {'file': open('_nf8VNRdtlCse1yloaZqM0ykXQA-001_1627013194.csv', 'rb')}

values = {'device_id': 'd_1234', 'timestamp':'1627013194', 'file_src': 'WATCH'}
response = requests.post(url, files=files, data=values)



files = {'file': open('_nf8VNRdtlCse1yloaZqM0ykXQA-001_1627027526.csv', 'rb')}

values = {'device_id': 'd_1234', 'timestamp':'1627027526', 'file_src': 'WATCH'}
response = requests.post(url, files=files, data=values)



files = {'file': open('_nf8VNRdtlCse1yloaZqM0ykXQA-001_1627034794.csv', 'rb')}
values = {'device_id': 'd_1234', 'timestamp':'1627034794', 'file_src': 'WATCH'}
response = requests.post(url, files=files, data=values)

files = {'file': open('_nf8VNRdtlCse1yloaZqM0ykXQA-001_1627041994.csv', 'rb')}
values = {'device_id': 'd_1234', 'timestamp':'1627041994', 'file_src': 'WATCH'}
response = requests.post(url, files=files, data=values)

files = {'file': open('_nf8VNRdtlCse1yloaZqM0ykXQA-001_1627027594.csv', 'rb')}
values = {'device_id': 'd_1234', 'timestamp':'1627027594', 'file_src': 'WATCH'}
response = requests.post(url, files=files, data=values)


print(response)
