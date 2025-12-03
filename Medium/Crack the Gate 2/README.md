## Crack the Gate 2

<img src="images/chall.png" width=600>

We are given a simple login page with rate limiting.  

<img src="images/webpage.png" width=400>

The challenge also provides us with a list of passwords to try against the login page.  

<img src="images/passwords.png" width=300>

Submitting the wrong password immediately leads to us being banned for 20 minutes. Clearly, manual bruteforce isn't feasible.  

<img src="images/ratelimit.png" width=600>

The challenge hints at us having to use the `X-Forwarded-For` header to rotate fake IP addresses for each login attempt.  

<img src="images/hint.png" width=400>

We can write a simple script to generate a random IP address each time and pass it through the `X-Forwarded-For` header, then bruteforce every password until the flag is found on the webpage.  

<img src="images/solve.png" width=400>

Flag: `picoCTF{xff_byp4ss_brut3_f6cca7d4}`