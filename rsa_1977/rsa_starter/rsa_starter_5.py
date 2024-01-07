# I've encrypted a secret number for your eyes only using your public key parameters:
# Use the private key that you found for these parameters in the previous challenge to decrypt this ciphertext:

p = 857504083339712752489993810777
q = 1029224947942998075080348647219

# N = p * q
N = 882564595536224140639625987659416029426239230804614613279163
# public key = N, e
e = 65537

# d to jest multiplicative inverse of `e` mod totient of `N`
totient = (p-1)*(q-1)

# d = e^-1 (mod Totient) ====> e*e^-1 === 1 (mod Totient)
d = pow(e, -1, totient) # 121832886702415731577073962957377780195510499965398469843281 z poprzedniego zadania

# skoro ciphertext = pow(message, e, N)
# to plaintext = pow(ciphertext, d, N)
c = 77578995801157823671636298847186723593814843845525223303932

print(pow(c,d,N))