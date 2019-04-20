import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols
from sympy.plotting import plot



N = 50
x = np.random.rand(N)
y = np.random.rand(N)
v = symbols('v')

x = np.linspace(-1,5)
y = -3.442*x + 6.025

plt.plot(x, y)
#p1 = plot(v*v)
x1 = [0.52,.91,-1.48,.01,-.46,.41,.53,-1.21,-.29,-.96]
y1 = [-1,0.32,1.23,1.44,-.37,2.04,.77,-1.1,0.96,0.08]

x2 = [2.46,3.05,2.2,1.89,4.51,3.06,3.16,2.05,2.34,2.94]
y2 = [2.59,2.87,3.04,2.64,-0.52,1.3,-0.56,1.54,0.72,0.13]
plt.scatter(x1, y1,color="red")
plt.scatter(x2, y2,color="blue")
plt.show()
