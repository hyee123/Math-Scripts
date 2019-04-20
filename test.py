from sympy import *
from sympy.plotting import plot
import matplotlib.pyplot as plt
x= Symbol('x')

function= x**4 + 7*x**3 + 8

#f = cos(x)

#p1 = plot(f)
x = list()
y = list()
x.append(1)
x.append(2)
x.append(3)
x.append(4)
y.append(1)
y.append(2)
y.append(3)
y.append(4)

plt.scatter(x,y)
plt.show()

#deriv= Derivative(f, x)
#deriv.doit()
#f2 = deriv.doit()

#f3 = diff(f)

#print f3
#print "\n"
#print f2.subs(x,3.14)
#print deriv.doit()
