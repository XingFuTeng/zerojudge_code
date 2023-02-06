a=int(input())
b=int(input())
y=-1
c=list(map(int,input().split(" ")))
for i in range(len(c)):
    x=c[i]
    print(a,end=" ")
    if i == len(c)-1:
        if x==a:
            print(": Drew at round %d"%int(i+1))
        elif (x==5 and a==0)or(x==2 and a==5)or(x==0 and a==2): 
            print(": Lost at round %d"%int(i+1))
        else:
            print(": Won at round %d"%int(i+1))
    else:
        if (x==0 and a==5)or(x==5 and a==2)or(x==2 and a==0): 
            print(": Won at round %d"%int(i+1))
            break
        elif (x==5 and a==0)or(x==2 and a==5)or(x==0 and a==2): 
            print(": Lost at round %d"%int(i+1))
            break
    if y==x:
        if x==0:
            a=5
        elif x==2:
            a=0
        elif x==5:
            a=2
    else:
        a=x
    y=x
