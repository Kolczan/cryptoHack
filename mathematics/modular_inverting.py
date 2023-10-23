def modular_inverting(g, p):
    for d in range(p):
        if (g * d) % p == 1:
            return d

g = 3
p = 13
print("Multilpicative inverse of g is: " + str(modular_inverting(g, p)))