from random import randint
from Crypto.Util.number import long_to_bytes

def adrien_signs():

    a = 288260533169915
    p = 1007621497415251

    FLAG = b'crypto{????????????????????}'


    def encrypt_flag(flag):
        ciphertext = []
        plaintext = ''.join([bin(i)[2:].zfill(8) for i in flag])
        for b in plaintext:
            e = randint(1, p)
            n = pow(a, e, p)
            if b == '1':
                ciphertext.append(n)
            else:
                n = -n % p
                ciphertext.append(n)
        return ciphertext


    print(encrypt_flag(FLAG))

    with open("mathematics/brainteasers/adrien_signs.txt", "r") as f:
        input = eval(f.read())

    res = ""
    for b in input:
        # Jeżeli to co teraz rozpatrujemy jest Quadratic Reside pierścienia p to tam wpisano 1
        legendre = pow(b, (p-1)//2, p)
        if legendre == 1:
            res += "1"
        else:
            # a jeśli nie to 0
            res += "0"

    print(long_to_bytes(int(res, 2)))