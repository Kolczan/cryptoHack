from sys import argv
from json import dumps, loads
from typing import Iterator

from pwn import connect
from sympy import factorint

from rsamath import b2i, i2b


HOST = "socket.cryptohack.org"
PORT = 13376

HCKSRC = b"admin=True"
HCK = b2i(HCKSRC)


def factor(n: int) -> Iterator[int]:
    factors = factorint(n)
    for fac, times in factors.items():
        for _ in range(times):
            yield fac


def sendjson(srv: connect, o: dict):
    srv.sendline(dumps(o).encode())


def recvjson(srv: connect) -> dict:
    return loads(srv.recvline(False).decode())


def recvany(srv: connect):
    srv.recvline()


factors = factor(HCK)

# host = host or HOST
# port = port or PORT
host = HOST
port = PORT
with connect(host, port) as srv:
    recvany(srv)
    sendjson(srv, {"option": "get_pubkey"})
    pubkey = recvjson(srv)
    n = int(pubkey["N"], 16)

    sig = 1
    for fac in factors:
        payload = {
            "option": "sign",
            "msg": i2b(fac).hex()
        }
        sendjson(srv, payload)
        sigj = recvjson(srv)
        sig *= int(sigj["signature"], 16)

    sig %= n
    payload = {
        "option": "verify",
        "msg": HCKSRC.hex(),
        "signature": i2b(sig).hex(),
    }
    sendjson(srv, payload)
    unsecret = recvjson(srv)

print(unsecret)


# if __name__ == "__main__":
#     if len(argv) >= 3:
#         main(argv[1], int(argv[2]))
#
#     else:
#         main(None, None)
