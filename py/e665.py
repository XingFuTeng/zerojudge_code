R=0
G=0
B=0
x=0
for i in range(int(input())):
    x=2**i
    R+=x//3+1
    B+=x//3
    if i%2==0:
        G+=x//3
    else:
        G+=x//3+1
print("%s %s %s"%(R,G,B))
