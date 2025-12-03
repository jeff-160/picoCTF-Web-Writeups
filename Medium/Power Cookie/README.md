## Power Cookie

<img src="images/chall.png" width=600>

We are given a simple gradebook webpage that gives us the option to login as a guest.  

<img src="images/webpage.png" width=600>

After continuing as a guest, we are redirected to a homepage with nothing interesting in particular.  

<img src="images/homepage.png" width=600>

However, when we can find a cookie `isAdmin` with a value set to `0`.  

<img src="images/cookie.png" width=500>

Changing the value of the cookie to `1` will give us admin privileges and display the flag.  

<img src="images/flag.png" width=600>

Flag: `picoCTF{gr4d3_A_c00k13_0d351e23}`