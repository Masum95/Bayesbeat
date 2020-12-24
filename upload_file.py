import requests


# files = {'file': open('sample.pdf', 'rb')}
files = {'file': open('_nf8VNRdtlCse1yloaZqM0ykXQA-001_16065070.csv', 'rb')}

values = {'device_id': '_nf8VNRdtlCse1yloaZqM0ykXQA', 'timestamp':'1606507099', 'file_src': 'WATCH'}


url = 'https://bayesbeat.herokuapp.com/file/upload/'
# url = 'http://127.0.0.1:8000/file/upload/'

response = requests.post(url, files=files, data=values)
files = {'file': open('uncle_March4.csv', 'rb')}

values = {'device_id': 'd_1234', 'timestamp':'1606507099'}
response = requests.post(url, files=files, data=values)

print(response)
