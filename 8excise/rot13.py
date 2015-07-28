def rot13(s):
    for i in s:
        
        if ord(i)+13 > 122:
            print chr(ord(i)-13)
        else:
            print chr(ord(i)+13)

rot13("alan Turing")

