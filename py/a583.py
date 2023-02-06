c=[]
a,b=map(int,input().split())
x=list(map(int,input().split()))
for i in range(b-1):
    for j in range(b-1-i):
        w=(x[2*i]-x[2*i+2*(j+1)])**2
        q=(x[2*i+1]-x[2*i+2*(j+1)+1])**2
        c.append(round((w+q)**0.5,4))
print("%.4f"%min(sorted(c)))
