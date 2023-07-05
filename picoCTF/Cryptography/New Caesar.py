# import string
import string

# constants
LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

# decode function
def b16_decode(cipher):
    dec = ""
    # loop through the cipher 2 characters at a time
    for c in range(0, len(cipher), 2):
        # turn the two characters into one binary string
        b = ""
        b += "{0:b}".format(ALPHABET.index(cipher[c])).zfill(4)
        b += "{0:b}".format(ALPHABET.index(cipher[c+1])).zfill(4)
        # turn the binary string to a character and add
        dec += chr(int(b,2))
    
    # return
    return dec

# unshift the text
def unshift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]

# encrypted flag
enc = "lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil"

# loop through all possible keys
for key in ALPHABET:
    # initialize string
    s = ""

    # loop through the encrypted text
    for i,c in enumerate(enc):
        # unshift it based on key
        s += unshift(c, key[i % len(key)])

    # decode
    s = b16_decode(s)

    # print key
    print(s)    

'''
maruf@mms:~/Documents/CTF/picoCTF/Cryptography$ py New\ Caesar.py 
ºÉ¤ÉÊ
     ¤¹·¸¸¹»¹
···
©¸¸¹sxwu¨¦zv§yzu|§¨{yªu¨t¦|w|wv¦z{¦xz
§¨bgfdiehidkjhdckfkfeijgi
qQqVUS
      XT
WXSZ
YWSR
    ZUZUT
         XY
           VX
v
`
@`EDBusGCtFGBItuHFwBuAsIDIDCsGHsEG
et_tu?_431db62c5618cd75f1d0b83832b67b46
TcNcd.N#" SQ%!R$% 'RS&$U S/Q'"'"!Q%&Q#%
CR=RS=B@AABDB@@@
2A,AB
???  ,1?00131
!01ûÿý .òþ/ñòýô/ óñ"ý ü.ôÿôÿþ.òó.ðò
/
/ ê
ïîìáíàáìãâàìëãîãîíáâïá
ùÙùÞÝÛ
ÑßÛÚ  ÐÜ
    ÒÝÒÝÜ
         ÐÑ
           ÞÐ
ÈèÍÌÊýûÏËüÎÏÊÁüýÀÎÿÊýÉûÁÌÁÌËûÏÀûÍÏ
íü×üý·×¼»¹ìê¾ºë½¾¹°ëì¿½î¹ì¸ê°»°»ºê¾¿ê¼¾
ÜëÆëì¦Æ«ª¨ÛÙ­©Ú¬­¨¯ÚÛ®¬Ý¨Û§Ù¯ª¯ª©Ù­®Ù«­
ËÚµÚÛµÊÈÊÊÈ
'''

# picoCTF{et_tu?_431db62c5618cd75f1d0b83832b67b46}