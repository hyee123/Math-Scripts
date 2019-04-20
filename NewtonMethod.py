from sympy import *

#setup symbols
x = Symbol('x')

#inputs
tolerance = 10**-5
f = x**2 -4*x + 3
P0 = 1.99

POld = P0
while True:
    fPrime = diff(f)
    PNew = POld - (f.subs(x,POld) / fPrime.subs(x,POld))

    print PNew
    if abs(PNew - POld) < tolerance:
        break
    POld = PNew
