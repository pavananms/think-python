def is_power(a,b):
    a=float(a)
    x=a/b
    if x==1:
        return True
  
    elif x<1:
        return False

    return is_power(x,b)
        
is_power(10,3)    
