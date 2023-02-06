x=list(map(int,input().split(" ")))
a=x[0]
b=x[1]
c=x[2]
if a==0 and b==0 and c!=0:
    print("IMPOSSIBLE")
elif a==0 and b==0 and c==0:
    print("AND")
    print("OR")
    print("XOR")
elif a!=0 and b!=0 and c==0:
    print("XOR")
elif (a==0 or b==0)and c==1:
    print("OR")
    print("XOR")
elif a!=0 and b!=0:
    print("AND")
    print("OR")
else:
    print("AND")
