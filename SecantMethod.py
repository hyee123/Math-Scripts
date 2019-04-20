from sympy import *
import math

#setup symbols
x = Symbol('x')
e = math.e
#inputs
tolerance = 10**-5
f = 3*x - e**x
P0 = 1
P1 = 2


while True:
    fPrime = diff(f)
    P2 = P1 - ((f.subs(x,P1) * (P1 - P0)) / ((f.subs(x,P1) - (f.subs(x,P0)))))

    print P2
    if abs(P2 - P1) < tolerance:
        break
    P0 = P1
    P1 = P2
    
