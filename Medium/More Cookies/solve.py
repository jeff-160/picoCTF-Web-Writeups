import requests
from base64 import b64encode, b64decode
import re

url = "http://mercury.picoctf.net:10868/"

s = requests.Session()

# fetch cookie
s.get(url)

cookie = s.cookies['auth_name']

# cbc bit flip attack
cookie = b64decode(b64decode(cookie))

for i in range(len(cookie)):
    for bit in range(8):
        payload = bytearray(cookie)
        payload[i] ^= 1 << bit

        print(f"Trying bit {bit + 1} at index {i}/{len(cookie)}")

        res = requests.get(url, cookies={ 'auth_name': b64encode(b64encode(bytes(payload))).decode() })
        
        if "picoCTF{" in res.text:
            print("Flag:", re.findall(r'(picoCTF{.+})', res.text)[0])
            exit()