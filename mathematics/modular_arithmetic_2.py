def modular_arithmetic_2():
    a = pow(3,17)
    b = 17
    c = a % b
    x = pow(5,17)
    y = 17
    z = x % y

    s = pow(7,16)%17
    print("3^17 % 17 daje reszte " + str(c) + ", 5^17 % 17 daje reszte " + str(z))
    print("7^16 % 17 daje reszte " + str(s))
    print("Małe twierdzenie Fermata, jak wykladnik jest o 1 mniejszy od  %mod, to reszta jest zawsze 1")
    print("Zakladajac ze q,p są liczbami pierwszymi, czyli coś typu q^p%p --> q, q^p-1 % p --> 1")