def modular_inverting(g, p):
    for d in range(p):
        if (g * d) % p == 1:
            return d
    print("Multilpicative inverse of g is: " + str(modular_inverting(g, p)))

# a^(p-1) = 1 mod p
# a^(p-2) = a^-1 mod p
# 3 * d = 1 mod 13
# Jak znalezc modular multiplicative inverse
# 3^(13-2) % 13 = 9  => 9 jest