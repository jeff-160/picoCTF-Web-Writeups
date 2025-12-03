## JAuth

<img src="images/chall.png" width=600>

We are given a webpage with a simple login page.  

<img src="images/webpage.png" width=600>

Upon logging in with the provided test credentials, we are redirected to an endpoint that doesn't seem very helpful.  

<img src="images/login.png" width=600>

However, if we check the webpage cookies, we will find a JWT token.  

<img src="images/jwt.png" width=400>

One of the challenge hints gives us a big clue. JWT tokens always have two `.` delimiters, and the text after the second one is the signature. This points us towards an alg none attack, where the signature is left empty, letting us bypass authentication entirely.  

<img src="images/hint.png" width=400>

To generate our malicious JWT token, we can first set the algorithm in our token header to `none`, then update our role in the token payload to `admin`.  

<img src="images/solve.png" width=600>

Changing the `token` cookie in the webpage will then display the flag.  

<img src="images/flag.png" width=600>

Flag: `picoCTF{succ3ss_@u7h3nt1c@710n_3444eacf}`