from sympy import *
x= Symbol('x')

f = 1/(1+x)

F = integrate(f,x)

F1 = F.subs(x,1).evalf() - F.subs(x,0).evalf()
i = 0
n = 80.0
h = 1.0/n
area = 0
while (True):
#    print h/2.0
 #   print (f.subs(x,i) + f.subs(x,i+h)) * (h/2)
    area += (h/2)*(f.subs(x,i) + f.subs(x,i+h))
    i += 1/n

    if(i >= 1):
        break

b = abs(area - F1) 

print area
print b
print b * n**2
