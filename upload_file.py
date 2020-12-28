import requests
url = 'http://127.0.0.1:8000/file/upload/'
# url = 'https://bayesbeat.herokuapp.com/file/upload/'


files = {'file': open('_nf8VNRdtlCse1yloaZqM0ykXQA-001_1606876164.csv', 'rb')}

values = {'device_id': 'd_1234', 'timestamp':'1606876164', 'file_src': 'WATCH'}
response = requests.post(url, files=files, data=values)



files = {'file': open('_nf8VNRdtlCse1yloaZqM0ykXQA-001_1606507067.csv', 'rb')}

values = {'device_id': 'd_1234', 'timestamp':'1606507067', 'file_src': 'WATCH'}
response = requests.post(url, files=files, data=values)



files = {'file': open('_nf8VNRdtlCse1yloaZqM0ykXQA-001_1606875804.csv', 'rb')}
values = {'device_id': 'd_1234', 'timestamp':'1606875804', 'file_src': 'WATCH'}
response = requests.post(url, files=files, data=values)


print(response)
