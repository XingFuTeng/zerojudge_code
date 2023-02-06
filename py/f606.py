d=[]
x=[]
little=0
big=[]
a=list(map(int,input().split()))
for i in range(a[0]):
    y=list(map(int,input().split()))
    x.append(y)
for i in range(a[2]):
    m=list(map(int,input().split()))
    for w in range(a[1]):
        d.append([w]+[0])
        
    for j in range(a[0]):
        for n in range(a[1]):
            d[n][1]+=x[j][n]
            print(d)
        if m[j]==d[m[j]][0]:
            little+=d[m[j]][1]
        elif d[m[j]][1]<=1000:
            little+=3*(x[j][n])
        elif d[m[j]][1]>1000:
            little+=3*1000+2*((d[m[j]][1])-1000)
        print(little)
        for i in range(a[1]):
            d[i][1]=0
    big.append(little)
    little=0
    d.clear()
print(big)
