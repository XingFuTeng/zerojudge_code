b=[]
try:
    while True:
        a=hash(input())
        b.append(a)
        if len(b)>1:
            for i in range(len(b)-1):
                if a == b[i]:
                    print(i)
                    print(a)
                    break
                    
except EOFError:
    pass

    
