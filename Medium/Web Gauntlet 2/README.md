## Web Gauntlet 2

<img src="images/chall.png" width=600>

We are given a login page that is vulnerable to SQLi.  

<img src="images/login.png" width=600>

`filter.php` also shows the exact blacklist being implemented.  

<img src="images/filter.png" width=600>

We can bypass the login with a simple SQLi payload.  

```
Username: ad'||'min
Password: a' is not 'b
```

Revisiting `filter.php` then reveals the flag.  

<img src="images/flag.png" width=600>

Flag: `picoCTF{0n3_m0r3_t1m3_86f3e77f3c5a076866a0fdb3b29c52fd}`