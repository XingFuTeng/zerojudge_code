a,b=map(int,input().split(" "))
if a!=b:
    x=a-b
    if x<b:
        print(x,end="+")
        print(b,end="=")
        print(a)
    else:
        print(b,end="+")
        print(x,end="=")
        print(a)
else:
    x=a-3
    b=a-x
    if x<b:
        print(x,end="+")
        print(b,end="=")
        print(a)
    else:
        print(b,end="+")
        print(x,end="=")
        print(a)
