import base64
from Crypto.Util.number import long_to_bytes
from pwn import *
def ascii():
    arr = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
    s = ""
    for i in arr:
        a = chr(i)
        s += a
    print(s)

def hexy():
    key2 = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
    print(str(bytes.fromhex(key2),'utf-8'))

def b64():
    key = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
    result = base64.b64encode(bytes.fromhex(key))
    print(str(result,'utf-8'))

def bytesandBigIntegers():
    key = int("11515195063862318899931685488813747395775516287289682636499965282714637259206269")
    a = long_to_bytes(key)
    print(a)


if __name__ == '__main__':
    ascii()
    hexy()
    b64()
    bytesandBigIntegers()
