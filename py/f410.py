al=[]
da=[]
x=int(input())
a=list(map(int,input().split()))
for i in range(x):
    if a[i]%2==0:
        al.append(a[i])
    else:
        da.append(a[i])
print(" ".join([str(_) for _ in sorted(al)]),end=" ")
print(" ".join([str(_) for _ in reversed(sorted(da))]))
