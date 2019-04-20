from sympy import *



x = Symbol('x')
f= 2**x

print diff(diff(diff(f)))
