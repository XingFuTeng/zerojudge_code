for i in range(int(input())):
    input()
    x=list(map(int,input().split()))
    t=0
    for j in range(len(x)):
        w=x.index(j+1)
        x.pop(w)
        t+=w
    print("Optimal train swapping takes %d swaps."%t)
            
