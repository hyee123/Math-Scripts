from sympy import *
import math
e = math.e
#from sympy.plotting import plot
#import matplotlib.pyplot as plt
x= Symbol('x')

f= e**x
i = 2
while i <= 13:
    v = 10**(i * -1)
    a = f.subs(x, 0 + v )
    b = f.subs(x,0)
    c =  ((a-b)/v)
    print c
    print (1-c)
    print "\n"
    
    #print function.subs(x, 1/v)
    #print v;
    i = i + 2

#f = cos(x)

#p1 = plot(f)
#f3 = diff(f)

#print f3
#print "\n"
#print f2.subs(x,3.14)
#print deriv.doit()
