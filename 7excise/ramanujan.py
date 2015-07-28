import math
def factorial(n):
    if n<2:
        return 1
    else:
        recurse= factorial(n-1)
        result=n*recurse
        return result
def estimate_pi():
    constant=(2*math.sqrt(2))/9801
    k=0
    total=0
    while True:
	    
        numer=factorial(4*k)*(1103.0+26390*k)
        denom=(factorial(4)**4) * 396**(4**k)
        ret = constant*numer/denom
        total=total+ret
        if abs(total) < 1e-15:
            break
        k=k+1

    return 1/total



estimate_pi() 
print "from library:",
print math.pi
factorial(0)
           
        

        
