input()
a=list(map(int,input().split()))
x=0
for i in range(len(a)):
    x+=a[i]
    print(x,end=" ")
