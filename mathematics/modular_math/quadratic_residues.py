def quadratic_residues():

    #We say that an integer x is a Quadratic Residue if there exists an a such that a2 = x mod p. If there is no such solution, then the integer is a Quadratic Non-Residue.
    #If a^2 = x then (-a)^2 = x. So if x is a quadratic residue in some finite field, then there are always two solutions for a.

    ### Reszta kwadratowa modulo = quadratic residue
    p = 29
    ints = [14, 6, 11]

    qr = [a for a in range(p) if pow(a, 2, p) in ints]
    print(f"flag {(qr)}")

    #pow (a,b,c) = a^b % c

    # Dla 14 nie ma takiego a, żeby a^2 % 29 == 14
    # Dla 6 jest: a = 8, a^2 % 29 <==>  64 % 29 = 6
    # Dla 6 jest KOLEJNE :O a=21, a^2 % 29  <==> 441 % 29 = 6
    # Dla 11 nie ma takiego a, żeby a^2 % 29 == 14

    # Wypisanie wgl wszystkich Quadratic Residues piersienia modulo 29
    # for i in range(29):
    #     for a in range(29):
    #         if (a*a%19 == i):
    #             print(f"{i} to quadratic residue, bo {a}^2 mod 29 = {i}")

