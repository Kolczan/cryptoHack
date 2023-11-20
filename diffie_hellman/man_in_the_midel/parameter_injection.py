from sys import argv
from json import dumps, loads
from pwn import connect
from hashlib import sha1
from Crypto.Cipher.AES import new, MODE_CBC
from Crypto.Util.Padding import unpad


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

def sendjson(srv: connect, o: dict):
    srv.sendlineafter(b": ", dumps(o).encode())


def recvjson(srv: connect) -> dict:
    srv.recvuntil(b": ")
    return loads(srv.recvline(False).decode())


def parameter_injection():
    host = "socket.cryptohack.org"
    port = 13371
    with connect(host, port) as srv:
        alice = recvjson(srv)
        p = int(alice["p"], 16)
        g = int(alice["g"], 16)
        A = int(alice["A"], 16)

        middleman = {
            "p": alice["p"],
            "g": alice["g"],
            "A": alice["p"],  # makes v = 0
        }
        sendjson(srv, middleman)

        bob = recvjson(srv)
        B = int(bob["B"], 16)

        middleman2 = {
            "B": alice["p"],
        }
        sendjson(srv, middleman2)

        exchange = recvjson(srv)

    iv = mkbytesh(exchange["iv"])
    c = mkbytesh(exchange["encrypted_flag"])
    v = mkkey(0)
    m = decrypt(v, c, iv=iv, strip_pad=False)
    print(m)
