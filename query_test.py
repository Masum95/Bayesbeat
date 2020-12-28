from django.shortcuts import render
import requests
from rest_framework import status



# response = requests.get('http://127.0.0.1:8000/file/upload/?selective=true&phone_num=015214')
response = requests.get('http://127.0.0.1:8000/file/isValidPhone/?phone_num=01521')

print(response.status_code)

json_data = response.json()
print(json_data)
