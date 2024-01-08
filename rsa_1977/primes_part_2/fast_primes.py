from sys import argv
from math import gcd

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

from rsamath import priv_exp, dec, i2b, b2i


INPUT = "rsa_1977/primes_part_2/ciphertext.txt"
KEY = "rsa_1977/primes_part_2/key.pem"


output = INPUT
key =  KEY
with open(output, "rt") as f:
    c = f.read().strip()

c = b2i(bytes.fromhex(c))

with open(key, "rt") as f:
    k = f.read().strip()

k = RSA.import_key(k)
n, e = k.n, k.e
print("n =", n)
print("p = ", end="")
p = int(input())
print("q = ", end="")
q = int(input())
d = priv_exp(p, q, e)
rsa = RSA.construct((n, e, d))
ciph = PKCS1_OAEP.new(rsa)
m = ciph.decrypt(i2b(c))
print(m)



# This is ROCA vulnerability
# p = 51894141255108267693828471848483688186015845988173648228318286999011443419469
# q = 77342270837753916396402614215980760127245056504361515489809293852222206596161
