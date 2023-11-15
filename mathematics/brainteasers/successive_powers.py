def successive_powers():
    powers = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]
    primes = [919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    # Opiszę to zadanie, ponieważ wydaje mi się, iż rozwiązanie jest nietypowe.
    # Cryptohack hintował, aby użyć kartki i długopisu, więc pewnie istnieje jakieś szybkie i proste rozwiązanie wynikające z łatwo zauważalnej zależności
    # Ja za to zdecydowałem się na brute force, który wiem, że jestem zrobić w czasie skończonym

    # Zadanie byłoby zbyt proste gdyby wiadomo było że te 12 potęg to pierwsze 12 potęg, a nie losowo wybrane 12

    # Szukamy liczby pierwszej i liczby x
    def foo():
        # iteracja po liczbach pierwszych https://gist.github.com/cblanc/46ebbba6f42f61e60666
        for prime in primes:
            print(f"Prime: {prime}")
            # Teraz próbuje zgadnąć liczbę x (zakładam, ze jest ona większa niż 100 i najpierw sprawdzałem tylko do 1000 (akurat się udało :D))
            for x in range(100, 1000):
                k = 0  # licznik ile juz bylo poteg w ciagu (max.12)
                for i in range(1, 100):
                    power = pow(x, i, prime)  # obliczenie potęg: x^i % prime
                    if (power == powers[k]):
                        k += 1  # naliczam ile już potęg z rzędu zgadza się z potęgami w liście `powers`
                    else:
                        k = 0  # jak ciąg się przerwie (lub wgl nawet nie rozpocznie) no to licznik k=0
                    if k == 12:  # Jak 12 wyliczonych przeze mnie potęg zgodzi się z listą `powers` no to "mamy to"
                        print("Mamy to")
                        odp = (prime, x)
                        return odp

    print(foo())


### eleganckie solution (one of)
# The following integers: 588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237 are successive large powers of an integer x, modulo a three digit prime p.
# We're given a list of successive modular powers of an element x, that means that: 588⋅x≡665(mod p), 665⋅x≡216(mod p) and so on. In particular we have: 113⋅x≡642(modp) and 114⋅x≡851(modp).So, subtracting: x≡851−642=209(mod p).
# So we've found the value for x.
# To find p just take the first equation and replace the value for x: 588⋅209≡665(mod p) means that 588⋅209−665≡0(mod p), so: p|588⋅209−665=122227.
# if you factorize the last number you get: 122227=7*19*919.The only good cadidate is p=919.
#
# It could seems that choosing 113*x and 114*x equations is sort of cheating, a general solution is to select two coprime numbers and with the Extended Eucledian Algorithm one can find out the two integers needed to get the linear comnination to write 1 with the numbers the challenge gave you.