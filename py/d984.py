try:
    while True:
        a=list(map(int,input().split()))
        
        if max(a)>sum(a)-max(a):
            if a.index(max(a))==0:
                print("A")
            if a.index(max(a))==1:
                print("B")
            if a.index(max(a))==2:
                print("C")
        else:
            if a.index(sum(a)-max(a)-min(a))==0:
                print("A")
            if a.index(sum(a)-max(a)-min(a))==1:
                print("B")
            if a.index(sum(a)-max(a)-min(a))==2:
                print("C")
except EOFError:
    pass
            
        
