import math

Xa = 2
Ya = 2
Xb = 7
Yb = 5

def lengther():
    Xx = (Xb - Xa)**2
    Yy = (Yb - Ya)**2
    leng = (Xx + Yy) ** 0.5
    print("{:.3f}".format(leng))

lengther()