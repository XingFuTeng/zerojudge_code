a=[]
x=[]
for i in range(25):
    x.append(1)
a.append(x)
x=[]
for i in range(24):
    for j in range(24-i):
        if j ==0:
            x.append(a[-1][0]+a[-1][1])
        else:
            x.append(x[-1]+a[-1][j+1])
    a.append(x)
    x=[]
try:
    while True:
        z=int(input())
        if z == 0:
            print(0)
        else:
            print(a[z-1][0])
except EOFError:
    pass
