b=[]
x=False
try:
    while True:
        a=input()
        for i in range(len(b)):
            if a==b[i]:
                x=True
        if x==True:
            print("1")
        else:
            print("0")
            b.append(a)
        x=False
except EOFError:
    pass
            
