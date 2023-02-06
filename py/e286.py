a=sum(list(map(int,input().split())))
b=sum(list(map(int,input().split())))
c=sum(list(map(int,input().split())))
d=sum(list(map(int,input().split())))
print("%d:%d"%(a,b))
print("%d:%d"%(c,d))
if a>b:
    if c>d:
        print("Win")
    else:
        print("Tie")
else:
    if c>d:
        print("Tie")
    else:
        print("Lose")
