c=0
a,b=map(int,input().split())
while a>12:
    if b<=0:
        break
    a=a-10
    b=b-1
    c+=1
while b+a-1>=12:
    if b<=0:
        break
    b=b-(12-a)-1
    a=2
    c+=1
print(c)
