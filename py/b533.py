z=set()
w=set()
x=set()
y=set()
for i in range(int(input())):
    a=list(input())
    #print(a)
    w=1
    while True:
        if a[w]==" ":
            w+=2
            break
        x.add(a[w])
        w+=3
    while True:
        y.add(a[w])
        w+=1
        if a[w]=="}":
            break
        w+=2
    print(x,y)
    z=set(sorted(x | y))
    w=set(sorted(x & y)) if len(x & y) else "n"
    print(z,w)
    x=set()
    y=set()
            
            
