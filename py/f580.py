xx=0
yy=0
zz=0
xxx=0
yyy=0
zzz=0
w=[]
def front(x,y,z):
    newx=0
    newy=0
    newz=0
    newx=7-y
    newy=x
    newz=z
    return newx,newy,newz
def right(x,y,z):
    newx=0
    newy=0
    newz=0
    newz=x
    newx=7-z
    newy=y
    return newx,newy,newz
a,b=map(int,input().split(" "))
for i in range(a):
    w.append([1,4,2])
for i in range(b):
    p,q=map(int,input().split(" "))
    if q==-1:
        xx=w[p-1][0]
        yy=w[p-1][1]
        zz=w[p-1][2]
        w[p-1][0],w[p-1][1],w[p-1][2]=front(xx,yy,zz)
    if q==-2:
        xx=w[p-1][0]
        yy=w[p-1][1]
        zz=w[p-1][2]
        w[p-1][0],w[p-1][1],w[p-1][2]=right(xx,yy,zz)
    if p>0 and q>0:
        xx=w[p-1][0]
        yy=w[p-1][1]
        zz=w[p-1][2]
        xxx=w[q-1][0]
        yyy=w[q-1][1]
        zzz=w[q-1][2]
        w[p-1][0]=xxx
        w[p-1][1]=yyy
        w[p-1][2]=zzz
        w[q-1][0]=xx
        w[q-1][1]=yy
        w[q-1][2]=zz
for i in range(a):
    print(w[i][0],end=" ")
    
    
