"""
urllib.request
"""
import urllib.request
import json


payload = {
    'key1': 'value1',
    'key2': 'value2',
}

# GET

query = urllib.parse.urlencode(payload)
url = 'http://httpbin.org/get' + '?' + query

with urllib.request.urlopen(url) as f:
    r = json.loads(f.read().decode('utf-8'))
    print(f'GET RES: {r}')

# POST

payload = json.dumps(payload).encode('utf-8')
req = urllib.request.Request('http://httpbin.org/post', data=payload, method='POST', headers={'Content-Type': 'application/json'})
with urllib.request.urlopen(req) as f:
    r = json.loads(f.read().decode('utf-8'))
    print(f'POST RES: {r}')

# PUT

req = urllib.request.Request('http://httpbin.org/put', data=payload, method='PUT')
req.add_header('Content-Type', 'application/json')
with urllib.request.urlopen(req) as f:
    r = json.loads(f.read().decode('utf-8'))
    print(f'PUT RES: {r}')

# PATCH

req = urllib.request.Request('http://httpbin.org/patch', data=payload, method='PATCH', headers={'Content-Type': 'application/json'})
with urllib.request.urlopen(req) as f:
    r = json.loads(f.read().decode('utf-8'))
    print(f'PATCH RES: {r}')

# DELETE

req = urllib.request.Request('http://httpbin.org/delete', data=payload, method='DELETE', headers={'Content-Type': 'application/json'})
with urllib.request.urlopen(req) as f:
    r = json.loads(f.read().decode('utf-8'))
    print(f'DELETE RES: {r}')

# GET

req = urllib.request.Request(f'http://httpbin.org/get?{query}', method='GET', headers={'Content-Type': 'application/json'})
with urllib.request.urlopen(req) as f:
    r = json.loads(f.read().decode('utf-8'))
    print(f'GET RES: {r}')