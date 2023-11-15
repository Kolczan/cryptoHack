from sys import argv

from safeparse import extract_values
from legendre import leg, leg_sqrt, is_qres


INPUT = "artifacts/output2.txt"  # must be valid python with p: int and ints: list[int]


def tonelli_shanks(a: int, p: int) -> tuple[int, int]:
    if not is_qres(a, p):
        return ()

    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1

    if s == 1:
        return leg_sqrt(a, p)  # case of = 3 mod 4

    for z in range(2, p):
        if leg(z, p) == p - 1:
            break

    c = pow(z, q, p)
    r = pow(a, (q + 1) // 2, p)
    t = pow(a, q, p)

    m = s
    t2 = 0
    while (t - 1) % p != 0:
        t2 = pow(t, 2, p)
        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break

            t2 = pow(t2, 2, p)

        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = pow(b, 2, p)
        t = (t * c) % p
        m = i

    # find both roots
    r0 = r
    r1 = -r % p

    return r0, r1


def main(input_file: str):
    vars = extract_values(input_file or INPUT)
    if vars is None:
        print("Could not load/parse values")
        return

    a0, a1 = tonelli_shanks(**vars)

    print("+a:", a0)
    print("-a:", a1)
    print()
    print("result:", min(a0, a1))


if __name__ == "__main__":
    main(argv[1] if len(argv) > 1 else None)
