"""
requests
"""
import requests


payload = {'key1': 'value1', 'key2': 'value2'}

# GET
res = requests.get('http://httpbin.org/get', params=payload)
print(f'RES: {res}')
print(f'STATUS_CODE: {res.status_code}')
print(f'TEXT: {res.text}')
print(f'JSON: {res.json()}')

# POST
res = requests.post('http://httpbin.org/post', data=payload, headers={'Content-Type': 'application/json'})
print(f'RES: {res}')
print(f'STATUS_CODE: {res.status_code}')
print(f'TEXT: {res.text}')
print(f'JSON: {res.json()}')

# PUT
res = requests.put('http://httpbin.org/put', data=payload)
print(f'RES: {res}')
print(f'STATUS_CODE: {res.status_code}')
print(f'TEXT: {res.text}')
print(f'JSON: {res.json()}')

# PATCH
res = requests.patch('http://httpbin.org/patch', data=payload)
print(f'RES: {res}')
print(f'STATUS_CODE: {res.status_code}')
print(f'TEXT: {res.text}')
print(f'JSON: {res.json()}')

# DELETE
res = requests.delete('http://httpbin.org/delete', data=payload)
print(f'RES: {res}')
print(f'STATUS_CODE: {res.status_code}')
print(f'TEXT: {res.text}')
print(f'JSON: {res.json()}')

# Timeout
from requests.exceptions import ConnectTimeout
try:
    res = requests.get('http://httpbin.org/get', params=payload, timeout=0.001)
    print(f'RES: {res}')
    print(f'STATUS_CODE: {res.status_code}')
    print(f'TEXT: {res.text}')
    print(f'JSON: {res.json()}')
except ConnectTimeout as e:
    print(f'handled exception: {e}')
    
