from Crypto.Util.number import long_to_bytes
def bytesandBigIntegers():
    key = int("11515195063862318899931685488813747395775516287289682636499965282714637259206269")
    a = long_to_bytes(key)
    print(a)