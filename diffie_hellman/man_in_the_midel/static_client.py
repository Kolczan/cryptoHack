# from sys import argv
# from json import dumps, loads
# from hashlib import sha1
#
# import pwnlib.tubes.remote
# from Crypto.Cipher.AES import new, MODE_CBC
# from Crypto.Util.Padding import unpad
# from pwn import connect
# from sympy.ntheory.residue_ntheory import discrete_log
#
# def mkkey(secret: int) -> bytes:
#     return sha1(str(secret).encode()).digest()[:16]
# def mkbytesi(data: int) -> bytes:
#     return data.to_bytes((data.bit_length() + 7) // 8)
# def mkbytesh(data: str) -> bytes:
#     return bytes.fromhex(data)
# def decrypt(k: bytes, c: bytes, *, iv: bytes = None, strip_pad: bool = True) -> bytes:
#     aes = new(k, MODE_CBC, iv=iv)
#     m = aes.decrypt(c)
#
#     return m if not strip_pad else unpad(m, 16)
# def egcd(a: int, b: int) -> tuple[int, int, int]:  # ax+by=gcd(a,b); tuple is (x, y, gcd(a,b))
#     _s = 0
#     _os = 1
#     _r = b
#     _or = a
#
#     while _r != 0:
#         _q = _or // _r
#         _or, _r = _r, (_or - _q * _r)
#         _os, _s = _s, (_os - _q * _s)
#
#     if b != 0:
#         _t = (_or - _os * a) // b
#     else:
#         _t = 0
#
#     return (_os, _t, _or)
#
# def sendjson(srv: connect, o: dict):
#     srv.sendlineafter(b": ", dumps(o).encode())
#
#
# def recvjson(srv: connect) -> dict:
#     srv.recvuntil(b": ")
#     return loads(srv.recvline(False).decode())
#
# pwnlib.tubes.remote.connect
# def static_client():
#     # host = host or HOST
#     # port = port or PORT
#     host = "socket.cryptohack.org"
#     port = 13379
#     with connect(host, port) as srv:
#         alice = recvjson(srv)
#         bob = recvjson(srv)
#         exchange = recvjson(srv)
#
#         p = int(alice["p"], 16)
#         g = int(alice["g"], 16)
#         A = int(alice["A"], 16)
#         B = int(bob["B"], 16)
#         iv = mkbytesh(exchange["iv"])
#         c = mkbytesh(exchange["encrypted"])
#
#         me = {
#             "p": hex(p),
#             "g": hex(A),
#             "A": hex(0x01),
#         }
#         sendjson(srv, me)
#         bob2 = recvjson(srv)
#         B2 = int(bob2["B"], 16)
#         exchange2 = recvjson(srv)
#
#     v = pow(B2, 0x01, p)
#     v = mkkey(v)
#     m = decrypt(v, c, iv=iv)
#     print(m)


########################## adnrew
# ----------------------------------------D E C R Y P T----------------------------------- # obsługa decyrptowania wiadomości AES
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import json
from pwn import *


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')
# ----------------------------------------D E C R Y P T-----------------------------------
# ---------------------------------- J S O N    D E R U L O ------------------------------- #obsługa recv i send jsonów
def json_recv():
    line = remote.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    remote.sendline(request)
# ---------------------------------- J S O N    D E R U L O -------------------------------

# Connect at nc socket.cryptohack.org 13371
remote = remote('socket.cryptohack.org', 13373)

def static_client():
    remote.recv()
    res = json_recv()
    print(res) # dostajemy p g i A, skoro duże A to wiemy że od Alice

    p = int(res['p'], 16)
    g = int(res['g'], 16)
    A = int(res['A'], 16)

    print("BOB")

    remote.recvuntil('Intercepted from Bob: ')
    res = json_recv()
    print(res) # od Boba: B

    B = int(res['B'], 16)

    remote.recvuntil('Intercepted from Alice: ')
    res = json_recv()
    print(res) # Od Alice: iv oraz encrypted

    iv = res['iv']
    encrypted = res['encrypted']

    # do wywołania print(decrypt_flag(shared_secret, iv, encrypted_flag)) potrzebujemy shared_secret czyli b=pow(B,a,p)

    # Wysylam Bobowi jako Alice p,g,A, ale A daje 1, a g daje jako A
    remote.recvuntil('send him some parameters: ')
    json_send({'p': hex(p), 'g': hex(A), 'A': hex(1)})

    # Bob wysyła mi B, czyli pow(g,a,p)
    remote.recvuntil('Bob says to you: ')
    res = json_recv()
    print(res)

    # ale to co on mi wysyłał jako niby B, to tak naprawde jest `b` czyli jego secret, któego ja używam aby sobie decryptować flage
    # czyli oszukaliśmy go tym miszmaszem, żeby wysłał nam małe `b`, a myśli ze nam wysłał B, czysta matma
    shared_secret = int(res['B'], 16)


    print(decrypt_flag(shared_secret, iv, encrypted))