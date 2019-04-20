from sympy import *
import math
#import matplotlib.pyplot as plt

#setup symbols
x = Symbol('x')
e = math.e
pi = math.pi

#input area
f = 1 / (x**2 +1)
#x_k = -5 + x
x_k = 5*cos(x*pi/10)
k = 10


def duck(x):
    return x + 1



def nev(a,b,n):
    
    if(len(a) == 1):
        return a[0]

    lx = b[len(a)-1]
    rx = b[0]
    lb = b[0:len(a)-1]
    rb = b[1:len(a)]
    la = a[0:len(a)-1]
    ra = a[1:len(a)]
    print ((n-lx)*nev(la,lb,n) - (n-rx)*nev(ra,rb,n)) / (rx - lx)    
    return ((n-lx)*nev(la,lb,n) - (n-rx)*nev(ra,rb,n)) / (rx - lx)

i = 0
t_x = [0]* (k+1)
t_y = [0]* (k+1)
while( i <= k):
    t_x[i] = (x_k.subs(x,i)).evalf()
    t_y[i] = (f.subs(x,t_x[i])).evalf()
    i += 1



#print t_x
#print t_y
q = [1,1.3,1.5,2]
v = [.75,.63,.55,.49]
print nev(v,q,1.6)
x_list = list()
y_list = list()
j = -5
#x_list.append(5)
#x_list.append(3)
#print x_list
#while ( j <= 5):
#    x_list.append(j)
#    y = nev(t_y,t_x,j)
#    y_list.append(y)
#    j += .1
#print(x_list)

#plt.scatter(x_list,y_list)
#plt.show()

