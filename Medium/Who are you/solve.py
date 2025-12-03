import requests
import re
import html

url = 'http://mercury.picoctf.net:46199/'

headers = {
    'User-Agent': 'picobrowser',
    'Referer': url,
    "Date": 'Tue, 15 Nov 2018 12:45:26 GMT',
    'DNT': '1',
    'X-Forwarded-For': '31.3.152.55',   # swedish ip address
    'Accept-Language': 'sv-SE'
}

res = requests.get(url, headers=headers)

try:
    print(re.findall(r'(picoCTF{.+})', res.text)[0])
except:
    result = re.findall(r'">(.+)</h3>', res.text)[0]
    print(html.unescape(result))