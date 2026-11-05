It's a XOR cipher. 

https://www.dcode.fr/xor-cipher

We already know the key size: 4 bytes. 

When we scroll down after we put the hash and the key size, we notice this part:

"FCS@{3eafb1a880g802`b96ae0ba256e423:c27:71320cded1872080fbe26b3b2dce7}"
with the hex key "9f582363"

We clearly see that we are close to the flag. We can just bruteforce the key by increasing or decreasing its value. 

Indeed, the hex key for the flag is "9f582360" 

And we have the flag: 

`FCSC{3ebfb1b880d802cb96be0bb256f4239c27971310cdfd1842083fbe16b3a2dcf7}`
