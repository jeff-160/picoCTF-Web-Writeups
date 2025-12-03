## MatchTheRegex

<img src="images/chall.png" width=600>

In the webpage provided, we are supposed to submit a valid input to reveal the flag.  

<img src="images/webpage.png" width=600>

Inspecting the webpage source reveals that our input is run against a regex check. The regex pattern expects our input to start with `p`, followed by 5 arbitrary characters, then ending with `F` and an optional `!`  

<img src="images/regex.png" width=500>

We can easily craft a string that meets these requirements.  

```
p_____F
```

Submitting the string will produce an `alert` with the flag.  

<img src="images/flag.png" width=600>

Flag: `picoCTF{succ3ssfully_matchtheregex_8ad436ed}`