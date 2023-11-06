# https://stackoverflow.com/questions/12826114/euclids-extended-algorithm-c
def egcd(a,b):
    if b == 0:
        return a, 1, 0

    nwd, u1, v1 = egcd(b, a % b)
    print(nwd, u1, v1)
    u = v1
    v = u1 - (a // b) * v1

    return nwd, u, v