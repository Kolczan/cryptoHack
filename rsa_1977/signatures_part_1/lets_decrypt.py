from sys import argv
from json import dumps, loads

from pwn import connect
from pkcs1.emsa_pkcs1_v15 import encode as pkcs1
from rsamath import b2i

HOST = "socket.cryptohack.org"
PORT = 13391

HCKSRC = "I am Mallory and I own CryptoHack.org"
HCK = pkcs1(HCKSRC.encode(), 256)
HCKNUM = b2i(HCK)


def sendjson(srv: connect, o: dict):
    srv.sendline(dumps(o).encode())


def recvjson(srv: connect) -> dict:
    return loads(srv.recvline(False).decode())


def recvany(srv: connect):
    srv.recvline()



host = HOST
port = PORT
with connect(host, port) as srv:
    recvany(srv)
    sendjson(srv, {"option": "get_signature"})
    signature = recvjson(srv)
    sig = int(signature["signature"], 16)
    n = sig - HCKNUM

    payload = {
        "option": "verify",
        "e": hex(1),
        "N": hex(n),
        "msg": HCKSRC
    }
    sendjson(srv, payload)
    unsecret = recvjson(srv)

print(unsecret)
