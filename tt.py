from math import sin, pi

def Simpson(f, a, b, n):
    if a > b:
        print 'Incorrect bounds'
        return None
    else:
    	h = (b - a)/float(n) # need to cast 'n' as float in order to avoid
        # integer division
    	sum1 = 0
    	for i in range(1, n/2 + 1):
        	sum1 += f(a + (2*i - 1)*h)
    	sum1 *= 4
    	sum2 = 0
    	for i in range(1, n/2): # range must be ints: range() integer 
            #end argument expected, got float.
        	sum2 += f(a + 2*i*h)
    	sum2 *= 2
    	approx = (b - a)/(3.0*n)*(f(a) + f(b) + sum1 + sum2)
    	return approx


def f(x):
    return 1/(x+1)

print Simpson(f,0,1,40 )
