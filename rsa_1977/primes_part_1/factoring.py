# Factorise the 150-bit number 510143758735509025530880200653196460532653147 into its two constituent primes. Give the smaller one as your answer.

import primefac
from sympy import factorint

N = 510143758735509025530880200653196460532653147
## to liczy bardzo długo, lepiej użyj http://factordb.com/ // translate this to eng broski

# method #1
# p, q = factorint(N).keys()
# print(p)
# print(q)
# print(min(p, q))

# method #2
# pnq = list(primefac.primefac(N,trial=1000,rho=42000,verbose=True))
#
# p = str(pnq[0]).strip('mqz(L)')
# q = str(pnq[1]).strip('mqz(L)')
# spacer = "-" * 64
# print(f"P: {0}".format(p))
# print(spacer)
# print(f"Q: {0}".format(q))



