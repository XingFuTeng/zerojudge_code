big=0
a=int(input())
x=list(map(int,input().split()))
for i in range(a):
    if x[i]==0:
        if i==0:
            big=big+x[1]
        elif i==a-1:
            big=big+x[-2]
        else:
            if x[i-1]<x[i+1]:
                big=big+x[i-1]
            else:
                big=big+x[i+1]
print(big)
