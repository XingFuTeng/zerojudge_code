al=[]
minn=1000000
a,b=list(map(int,input().split()))
m=[]
al.append([-1]*(b+2))
x=0
y=0
for i in range(a):
    m=[]
    c=list(map(int,input().split()))
    if minn>min(c):
        minn=min(c)
        x,y=i+1,c.index(min(c))+1
    m.append(-1)
    for j in range(len(c)):
        w=c[j]
        m.append(w)
    m.append(-1)
    al.append(m)
al.append([-1]*(b+2))
#print(al)
#print(x,y)
#print(minn)
p=minn
while True:
    m=[]
    l=0
    if al[x+1][y]!=-1:
        m.append(al[x+1][y])
    else:
        m.append(1000000)
        l+=1
    if al[x][y+1]!=-1:
        m.append(al[x][y+1])
    else:
        m.append(1000000)
        l+=1
    if al[x-1][y]!=-1:
        m.append(al[x-1][y])
    else:
        m.append(1000000)
        l+=1
    if al[x][y-1]!=-1:
        m.append(al[x][y-1])
    else:
        m.append(1000000)
        l+=1
    #print(al)
    #print(m)
    #print(x,y)
    if l==4:
        break
    if m.index(min(m))==0:
        al[x][y]=-1
        p+=m[0]
        x,y=x+1,y
    elif m.index(min(m))==1:
        al[x][y]=-1
        p+=m[1]
        x,y=x,y+1
    elif m.index(min(m))==2:
        al[x][y]=-1
        p+=m[2]
        x,y=x-1,y
    elif m.index(min(m))==3:
        al[x][y]=-1
        p+=m[3]
        x,y=x,y-1
print(p)

    

