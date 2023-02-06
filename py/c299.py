x=1
try:
    while True:
        a=list(map(int,input().split()))
        print(a[1],end=" ")
        for i in range(a[0]-2):
            print(a[2+i],end=" ")
            if a[2+i]!=a[2+i+1]:
                x=x-1
        if x!=1:
            print("no")
        else:
            print("yes")
        x=1
except EOFError:
    pass
