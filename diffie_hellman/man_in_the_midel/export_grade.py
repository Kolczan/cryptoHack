from sys import argv
from json import dumps, loads
from hashlib import sha1
from Crypto.Cipher.AES import new, MODE_CBC
from Crypto.Util.Padding import unpad
from pwn import connect
from sympy.ntheory.residue_ntheory import discrete_log

def mkkey(secret: int) -> bytes:
    return sha1(str(secret).encode()).digest()[:16]
def mkbytesi(data: int) -> bytes:
    return data.to_bytes((data.bit_length() + 7) // 8)
def mkbytesh(data: str) -> bytes:
    return bytes.fromhex(data)
def decrypt(k: bytes, c: bytes, *, iv: bytes = None, strip_pad: bool = True) -> bytes:
    aes = new(k, MODE_CBC, iv=iv)
    m = aes.decrypt(c)

    return m if not strip_pad else unpad(m, 16)
def egcd(a: int, b: int) -> tuple[int, int, int]:  # ax+by=gcd(a,b); tuple is (x, y, gcd(a,b))
    _s = 0
    _os = 1
    _r = b
    _or = a

    while _r != 0:
        _q = _or // _r
        _or, _r = _r, (_or - _q * _r)
        _os, _s = _s, (_os - _q * _s)

    if b != 0:
        _t = (_or - _os * a) // b
    else:
        _t = 0

    return (_os, _t, _or)

def sendjson(srv: connect, o: dict):
    srv.sendlineafter(b": ", dumps(o).encode())


def recvjson(srv: connect) -> dict:
    srv.recvuntil(b": ")
    return loads(srv.recvline(False).decode())


def export_grade():
    # host = host or HOST
    # port = port or PORT
    host = "socket.cryptohack.org"
    port = 13379
    with connect(host, port) as srv:
        alice_support = recvjson(srv)
        alice_support = alice_support["supported"]
        support = min(int(x[2:]) for x in alice_support)
        support = "DH" + str(support)
        support = {"supported": [support]}

        sendjson(srv, support)
        chosen = recvjson(srv)
        sendjson(srv, chosen)

        alice = recvjson(srv)
        bob = recvjson(srv)
        exchange = recvjson(srv)

        p = int(alice["p"], 16)
        g = int(alice["g"], 16)
        A = int(alice["A"], 16)
        B = int(bob["B"], 16)
        iv = mkbytesh(exchange["iv"])
        c = mkbytesh(exchange["encrypted_flag"])

    print(f"solve for g=0x{g:02X} A=0x{A:016X} p=0x{p:016X}")
    a = discrete_log(p, A, g)
    print("solved")

    v = pow(B, a, p)
    v = mkkey(v)
    m = decrypt(v, c, iv=iv, strip_pad=False)

    print(m)
# This is a discrete logarithm problem
