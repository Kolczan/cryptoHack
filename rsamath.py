from random import randint
from math import gcd,isqrt

from sympy import factorint

__all__ = [
    "b2i",
    "i2b",
    "euler_totient",
    "priv_exp",
    "factor",
    "enc",
    "dec",
    "pq_from_d",
]


def b2i(b: bytes) -> int:
    return int.from_bytes(b)


def i2b(i: int) -> bytes:
    return i.to_bytes((i.bit_length() + 7) // 8)


def euler_totient(p: int, q: int) -> int:
    return (p - 1) * (q - 1)


def priv_exp(p: int, q: int, e: int=65537) -> int:
    lambda_n = euler_totient(p, q)
    return pow(e, -1, lambda_n)


def factor(n: int) -> list[int]:
    factors = factorint(n)
    return list(factors.keys())


def enc(m: int, e: int, n: int) -> int:
    return pow(m, e, n)


def dec(c: int, d: int, n: int) -> int:
    return pow(c, d, n)


def pq_from_d(d: int, e: int, n: int) -> tuple[int]:
    k = d * e - 1
    while True:
        g = randint(1, n)
        t = k
        while t % 2 == 0:
            t //= 2
            x = pow(g, t, n)
            if x > 1 and (y := gcd(x - 1, n)):
                p = y
                q = n // p
                return p, q

def fermat(n: int) -> tuple[int, int]:
    m = int(isqrt(n))
    m = m + 1
    t = m
    y = int(isqrt(t * t - n))
    while (y * y) != (t * t - n):
        t += 1
        y = int(isqrt(t * t - n))

    return t + y, t - y
