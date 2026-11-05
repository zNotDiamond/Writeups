It's a chinese remainder cypher. 
https://www.dcode.fr/chinese-remainder
We must copy the modulos on the right side. 
The modulos, in the python script, are after the % symbol. 
For instance:
print("carotte = ", int.from_bytes(key) % 17488856370348678479)
print("radis   = ", int.from_bytes(key) % 16548497022403653709)
print("tomate  = ", int.from_bytes(key) % 17646308379662286151) 
[...]
The first modulo would be "17488856370348678479", the second one is "16548497022403653709" and so on..

On the left side of the board, we must enter the remaiders, that are in the output file:
carotte =  392278890668246705
radis   =  4588810924820033807
tomate  =  17164682861166542664
pomme   =  12928514648456294931
banane  =  5973470563196845286

As a result output, we have this value: x=58537804506201655097879135670024677446002384165465965481902712238119765745741

At last, we have the key in order to decrypt our hash (2da1dbe8c3a739d9c4a0dc29a27377fe8abc1c0feacc9475019c5954bbbf74dcedce7ed3dc3ba34fa14a9181d4d7ec0133ca96012b0a9f4aa93c42c61acbeae7640dd101a6d2db9ad4f3b8ccfe285e0d)

We have clues about what decryption type the hash is. line 13 of the scrypt: "AES.new(key, AES.MODE_ECB)" So it's clearly an AES encryption type with a ECB variant. 

First, we convert it to hex. The length is clearly 256 bits:
816b392538ae5895093e0a8094a2b858a1c2bdc16587ebfbd80fd50f7e19204d

Then we put our hash in a txt file, that we must convert to binary. We used xxd here:
echo -n "2da1dbe8c3a739d9c4a0dc29a27377fe8abc1c0feacc9475019c5954bbbf74dcedce7ed3dc3ba34fa14a9181d4d7ec0133ca96012b0a9f4aa93c42c61acbeae7640dd101a6d2db9ad4f3b8ccfe285e0d" >  Carrote_Radis_Tomate.txt 

xxd -r -p Carrote_Radis_Tomate.txt > Carrote_Radis_Tomate.bin

Then we decrypt our hash with openssl:
openssl enc -d -aes-256-ecb -K 816b392538ae5895093e0a8094a2b858a1c2bdc16587ebfbd80fd50f7e19204d -in Carrote_Radis_Tomate.bin`
