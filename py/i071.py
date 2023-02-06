a,b=map(int,input().split())
x=list(map(int,input().split()))
w=0
p=0
for i in range(a-b):
    if x[b+i]>w and x[b+i]>x[b-1]:
        w=x[b+i]
        p+=1
w=0
for i in range(b-1) :
    if x[b-2-i]>w and x[b-2-i]>x[b-1]:
        w=x[b-2-i]
        p+=1
print(p)
