buy=1
w=0
pr=0
a,b=map(int,input().split(" "))
x=list(map(int,input().split(" ")))
for i in range(a-1):
    if buy==1:
        if x[i+1]>=x[w]+b:
            pr=pr+x[i+1]-x[w]
            w=i+1
            buy=buy-1
    elif buy==0:
        if x[i+1]<=x[w]-b:
            w=i+1
            buy=buy+1
print(pr)
        
        
