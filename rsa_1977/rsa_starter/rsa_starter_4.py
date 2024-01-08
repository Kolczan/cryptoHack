# N = p * q
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
# public key = N, e
e = 65537

# tocjent = funkcja phi Eulera dla liczb pierwszych ma postać (p-1)(q-1)
totient = (p-1)*(q-1)

# d to jest multiplicative inverse of `e` modulo the totient of `N`
# d = e^-1 (mod Totient) ====> e*e^-1 === 1 (mod Totient)
d = pow(e, -1, totient)
print(d)