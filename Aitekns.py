from sympy import *
import math

#setup symbols
x = Symbol('x')
e = math.e
#inputs
tolerance = 10**-5
f = cos(x)
P0 = 1
i = 0


while i < 4:
    #calculate firt two points
    
    #fixed point
    
    P1 = f.subs(x, P0)
    P2 = f.subs(x, P1)

    print P0
    print P1.evalf()
    print P2.evalf()
    print "\n"

    Pnew = P0 - ((P1 - P0)**2)/ (P2 - 2*P1 + P0)

    P0 = Pnew.evalf()
    i += 1
