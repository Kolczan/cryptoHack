import pwnlib
import json
import pwn

def json_recv(remote):
    line = remote.recvline()
    return json.loads(line.decode())

def test_connection():
    remote = pwn.remote('socket.cryptohack.org',13380)
    # remote = pwnlib.tubes.remote.connect('socket.cryptohack.org', 13380)
    remote.recvuntil('Intercepted from Alice: ')
    res = json_recv(remote)
    print(res) # Alice: p g A