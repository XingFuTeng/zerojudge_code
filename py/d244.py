a=sorted(list(map(int,input().split())))
for i in range(len(a)//3):
    if a[3*i]!=a[3*i+1] or a[3*i+1]!=a[3*i+2] or a[3*i+2]!=a[3*i]:
        print(a[3*i])
        break
