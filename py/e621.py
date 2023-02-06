for i in range(int(input())):
    a=list(map(int,input().split()))
    x=[]
    for y in range(a[1]-a[0]-1):
        if (a[0]+y+1)%(a[2])!=0:
            x.append(str(a[0]+y+1))
    if len(x):
        print(' '.join(x))
    else:
        print("No free parking spaces.")
