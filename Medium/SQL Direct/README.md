## SQL Direct  

<img src="images/chall.png" width=600>

When we first connect to the server, we can run `\l` to list the databases, and we can see that we are currently in the `pico` database.  

<img src="images/db.png" width=600>

We can then run `\dt` to list the tables in `pico`, revealing a `flags` table.  

<img src="images/tables.png" width=600>

We can read the entries in the `flags` table with `select * from flags;`, which will give us our flag.  

<img src="images/flag.png" width=600>

Flag: `picoCTF{L3arN_S0m3_5qL_t0d4Y_31fd14c0}`