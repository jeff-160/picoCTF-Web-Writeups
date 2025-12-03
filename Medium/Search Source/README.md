## Search Source

<img src="chall.png" width=600>

bruh this chall stupid asf  

just mirror the website locally with `httrack` then use `grep` to search for the flag  

```bash
httrack http://saturn.picoctf.net:53521/ -O ./test

grep -ri 'picoCTF{' ./test
```

Flag: `picoCTF{1nsp3ti0n_0f_w3bpag3s_ec95fa49}`