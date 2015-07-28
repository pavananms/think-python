
def has_no_e(s):
    for i in s:
        if i == 'e':
            return False
    return True

def ab20():
    c=0
    t=0
    fin=open('words.txt')
    for i in fin:
        t=t+1
        if has_no_e(i):
            print i
            c=c+1
    
    percent=(c*100.0)/t
    print "percentage:%d,%d,%d"%(percent,c,t)


ab20()
