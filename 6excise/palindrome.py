def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def palindrome(word):
    f=first(word)
    l=last(word)
    mid=middle(word)
    if len(word) > 2:
	if f != l:
	   return False
        else:
	   return palindrome(mid)
    
    else:
        
	if f == l:
	   return True
        else:
           return False
	       
	        
