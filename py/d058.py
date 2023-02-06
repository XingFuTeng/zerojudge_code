try:
    while True:
        a=input()
        if a==0:
            break
        
        
        elif a.isalpha()!=True:
            print("Fail")
            w=0
            pass
        else:
            x=a.upper()
            z=list(x)
            w=0
            for i in range(len(x)):
               w+=ord(z[i])-64
            if w>0:
                print(w)
            else:
                print("Fail")
            w=0
except EOFError:
    pass
        
