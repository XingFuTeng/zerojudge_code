z=[]
y=[]
a,b=map(int,input().split(" "))
for i in range(a):
    x=list(map(int,input().split(" ")))
    y.append(max(x))
for i in range(len(y)):
    if sum(y)%y[i]==0:
        z.append(y[i])
print(sum(y))
if len(z):
    print(" ".join('%s' %id for id in z))
else:
    print("-1")
    
