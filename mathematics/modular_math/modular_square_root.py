def modular_square_root():
    a = 8479994658316772151941616510097127087554541274812435112009425778595495359700244470400642403747058566807127814165396640215844192327900454116257979487432016769329970767046735091249898678088061634796559556704959846424131820416048436501387617211770124292793308079214153179977624440438616958575058361193975686620046439877308339989295604537867493683872778843921771307305602776398786978353866231661453376056771972069776398999013769588936194859344941268223184197231368887060609212875507518936172060702209557124430477137421847130682601666968691651447236917018634902407704797328509461854842432015009878011354022108661461024768
    p = 30531851861994333252675935111487950694414332763909083514133769861350960895076504687261369815735742549428789138300843082086550059082835141454526618160634109969195486322015775943030060449557090064811940139431735209185996454739163555910726493597222646855506445602953689527405362207926990442391705014604777038685880527537489845359101552442292804398472642356609304810680731556542002301547846635101455995732584071355903010856718680732337369128498655255277003643669031694516851390505923416710601212618443109844041514942401969629158975457079026906304328749039997262960301209158175920051890620947063936347307238412281568760161

    def euler_criterion(a, p):
        return pow(a, (p - 1) // 2, p)

    def tonelli(a, p):
        # By factoring out powers of 2, find Q and S such that p-1 = Q*2^S with Q odd
        q = p - 1
        s = 0
        while q % 2 == 0:
            q //= 2
            s += 1
        if s == 1:
            return pow(a, ((p + 1) // 4), p)  # Tu mamy ten case, co był w poprzednim zadaniu
        # Musimy znaleźć jakieś Quadratic Non-Residue pierścienia `modulo p`
        for z in range(2, p):
            if p - 1 == euler_criterion(z, p):
                break
        # Jak już znaleźliśmy `z` to robimy kilka zmiennych
        m = s
        c = pow(z, q, p)
        t = pow(a, q, p)
        r = pow(a, (q + 1) // 2, p)
        # r = n^(q+1)/2 mod p
        # r^2 = a*t
        # t to 2^(M-1)-th root of 1
        # r to nasza 'próba' odgadnięcia pierwiastka
        # jeśli nie, to r=n*t, gdzie t jest 2^(M-1)-th pierwiastkiem 1
        # teraz musimy dla danego M (równego S) znając r i t możemy wykalkulować r i t dla M-1 powtarzamy to aż t stanie się 2^0-th pierwstakiem 1 wtedy r jest square root of a

        t2 = 0
        while (t - 1) % p != 0:
            t2 = (t * t) % p
            for i in range(1, m):
                if (t2 - 1) % p == 0:
                    break
                t2 = (t2 * t2) % p
            b = pow(c, 1 << (m - i - 1), p)
            r = (r * b) % p
            c = (b * b) % p
            t = (t * c) % p
            m = i
        return r

    print(tonelli(a, p))

# In Legendre Symbol we introduced a fast way to determine whether a number is a square root modulo a prime. We can go further: there are algorithms for efficiently calculating such roots. The best one in practice is called Tonelli-Shanks, which gets its funny name from the fact that it was first described by an Italian in the 19th century and rediscovered independently by Daniel Shanks in the 1970s.
# All primes that aren't 2 are of the form p ≡ 1 mod 4 or p ≡ 3 mod 4, since all odd numbers obey these congruences. As the previous challenge hinted, in the p ≡ 3 mod 4 case, a really simple formula for computing square roots can be derived directly from Fermat's little theorem. That leaves us still with the p ≡ 1 mod 4 case, so a more general algorithm is required.
# In a congruence of the form r^2 ≡ a mod p, Tonelli-Shanks calculates r.
# Tonelli-Shanks doesn't work for composite (non-prime) moduli. Finding square roots modulo composites is computationally equivalent to integer factorization - that is, it's a hard problem.
# The main use-case for this algorithm is finding elliptic curve co-ordinates. Its operation is somewhat complex so we're not going to discuss the details, however, implementations are easy to find and Sage has one built-in.