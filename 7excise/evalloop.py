def eval_loop():
    while True:
        s=raw_input("enter an expressionto evaluate :: ")
        if s=="done":
            break
        else: 
            a=eval(s)
            print a
    
    print a


