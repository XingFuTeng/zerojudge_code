a=list(map(int,input().split(" ")))
x=[]
y=1
for i in range(a[0]):
    x.append(i+1)
for i in range(a[2]):
    if y+a[1]-1>len(x):
        x.pop(len(x)-y-1)
        y=y-len(x)+a[1]
    else:
        x.pop(y+a[1]-2)
        y=y+a[1]-2
print(y)
