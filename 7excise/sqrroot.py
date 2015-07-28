import math
def sqrrt(a):
    if a==1:
      return 1.0
    x=a-1
    while a!=1:
        y = (x + a/x) / 2.0
        if abs(y-x) < 0.0000000000001:
            return x
            break
        x = y

def square_table():
    
    for i in range(10):
        a=sqrrt(i)
        print "%r    %r    %r" %(i,a,math.sqrt(i))

square_table()
