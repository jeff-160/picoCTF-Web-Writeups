## Irish Name Repo 1

<img src="images/chall.png" width=600>

We are given a webpage that lists irish people.  

<img src="images/webpage.png" width=600>

Opening the side menu reveals an admin panel we can access. We will then be redirected to a login page.  

<img src="images/login.png" width=600>

We can bypass the login with a simple SQLi payload.  

```
username: ' or 1--
password: abc
```

<img src="images/flag.png" width=600>

Flag: `picoCTF{s0m3_SQL_85832275}`