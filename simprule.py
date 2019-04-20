from sympy import *
x= Symbol('x')

f = 1/(1+x)

F = integrate(f,x)

F1 = F.subs(x,1).evalf() - F.subs(x,0).evalf()
i = 0.0
n = 10.0
h = 1.0/n
area = 0

#odd

while (True):
#    print h/2.0
 #   print (f.subs(x,i) + f.subs(x,i+h)) * (h/2)
    area += (h/6.0)*(f.subs(x,i) + 4.0*f.subs(x,(i+(h/2.0))) + f.subs(x,i+h))
    i += h

    if(i >= 1):
        break

b = abs(area - F1) 

print area 
print b
print b * n** 4
