a=int(input())
b=list(map(int,input().split(" ")))
y=0
x=a+1
z=1
while True:
    print(y)
    if z>=a:
        break
    while b[y]==x:
        x=b[b[y]]
        b.remove(b[y])
        x=y
        z=z+1
    y=y+1


        


