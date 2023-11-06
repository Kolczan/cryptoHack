def chinese_remainder_theorem():
    x = 0  # szukana liczba
    for i in range(935): # i to kandydaci na `x`
        # szukam takiego duzego `x` zeby spelnial wszystkie przystawania (conguerencje)
        if i % 5 == 2 and i % 11 == 3 and i % 17 == 5:
            x = i
    # W zadaniu trzeba znaleźć `a` a nie `x`, więc korzysta ze wzory `x % N = a`
    print("x: " + str(x))
    print("a: " + str(x % 935))








# In cryptography, we commonly use the Chinese Remainder Theorem to help us reduce a problem of very large integers into a set of several, easier problems.
# Given the following set of linear congruences:
#
# x ≡ 2 mod 5
# x ≡ 3 mod 11
# x ≡ 5 mod 17
#
# Find the integer a such that x ≡ a mod 935
# Starting with the congruence with the largest modulus, use that for x ≡ a mod p we can write x = a + k*p for arbitrary integer k.