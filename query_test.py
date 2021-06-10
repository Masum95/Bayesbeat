from django.shortcuts import render
import requests
from rest_framework import status



# response = requests.get('http://127.0.0.1:8000/file/upload/?selective=true&phone_num=015214')
# response = requests.get('http://127.0.0.1:8000/file/isValidPhone/?phone_num=01521')
url = 'http://127.0.0.1:8000/file/medical_profile/'
values = {'registration_id': '3d2594ec-7c88-4f9c-9c2c-3e4ddf9891be', 'height': '123', 'weight':'456', 'dob': '1956-01-01'}
response = requests.post(url, data=values)



print(response.status_code)

# json_data = response.json()
# print(json_data)
