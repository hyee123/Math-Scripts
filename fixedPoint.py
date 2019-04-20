
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
    P0 = P1
    print P0.evalf()
    i +=1
