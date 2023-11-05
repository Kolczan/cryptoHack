def quadratic_residues():
    # print("DLA 14")
    # for i in range(28):
    #     if (i*i%29 == 14):
    #         print(f"mam to {i}")
    # print("DLA 6")
    # for i in range(28):
    #     if (i*i%29 == 6):
    #         print(f"mam to {i}")
    # print("DLA 11")
    # for i in range(28):
    #     if (i*i%29 == 11):
    #         print(f"mam to {i}")

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

