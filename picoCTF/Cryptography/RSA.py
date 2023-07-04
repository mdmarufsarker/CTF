import gmpy

from Crypto.Util.number import *

from Crypto.PublicKey import RSA

from Crypto.Cipher import PKCS1_v1_5



msg = 'crypto here'

p = getPrime(128)

q = getPrime(128)

n = p*q

e = getPrime(64)

pubkey = RSA.construct((long(n), long(e)))

privatekey = RSA.construct((long(n), long(e), long(d), long(p), long(q)))

key = PKCS1_v1_5.new(pubkey)

enc = key.encrypt(msg).encode('base64')

key = PKCS1_v1_5.new(privatekey)

msg = key.decrypt(enc.decode('base64'), e)
