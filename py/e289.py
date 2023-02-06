m,n=map(int,input().split())
data_1=list(map(int,input().split()))
data_2=dict()
b=0
for i in range(n-m+1):
    for j in range(m):
        ans=data_2.get(data_1[i+j])
        if ans==None or data_2[data_1[i+j]]==0:
            data_2[data_1[i+j]]=1
    value=data_2.values()
    if sum(value)==m:
        b+=1
    data_2.pop(data_1[i])
print(b)
