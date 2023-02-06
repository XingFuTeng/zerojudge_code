x=False
y=False
z=0
k=str
a=list(map(int,input().split(" ")))
for i in range(a[0]):
    c=input()
    b=list(c)
    if i+1==a[2]:
        if a[2]==a[4]:
            A=(b[a[3]-1:a[5]])
            StrA = "".join(A)
            print(StrA)
        elif a[3]==a[5]:
            print(b[a[3]-1],end="")
            x=True
        else:
            print(b[a[3]-1],end="")
            y=True
            z+=1
    elif x and a[4]>i:
        print(b[a[3]-1],end="")
    elif y and a[4]>i:
        print(b[a[3]+z-1],end="")
        z+=1
