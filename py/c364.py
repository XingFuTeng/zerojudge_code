from itertools import accumulate
a=int(input())
x=list(map(int,input().split()))
dp=[]
ans=[]
acc=[0]+list(accumulate(x))
j=1
for i in range(a):
    dp.append(0)
    while True:
        if i-j<0:
            j=0
            break
        if x[i-j]>x[i]:
            j=0
            break
        if x[i-j]<x[i]:
            dp[-1]+=1
        j+=1
        #print(x[i-j])
    #print()
#print(dp)
for i in range(a):
    ans.append(acc[i]-acc[i-dp[i]])
dp=[]
j=1
for i in range(a):
    dp.append(0)
    while True:
        if i+j>a-1:
            j=0
            break
        if x[i+j]>x[i]:
            j=0
            break
        if x[i+j]<x[i]:
            dp[-1]+=1
        j+=1
#print(dp)
for i in range(a):
    ans[i]+=acc[i+dp[i]+1]-acc[i+1]
for i in range(a):
    print(ans[i])
