x=[]
t=[]
zz=[]
a=list(input())
b=list(map(int,input()))
for i in range(len(a)):
    if ord(a[i])>91:
        a[i]=ord(a[i])-32
    else:
        a[i]=ord(a[i])
        
    if a[i] in t:
        x[t.index(a[i])]+=b[i]
    else:
        x.append(b[i])
        t.append(a[i])
for i in range(len(a)):
    zz.append(0)
for i in range(len(t)):
    z=x[i]%a.count(t[i])
    for j in range(len(a)):
        if a[-j-1]==t[i]:
            if z>0:
                zz[j]=int(x[i]/a.count(t[i])+1)
                z-=1
            else:
                zz[j]=int(x[i]/a.count(t[i]))
for i in range(len(zz)):
    print(zz[-i-1],end="")
  
