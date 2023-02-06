a=b=c=0
b=list(map(int,input().split(" ")))
x=sorted(b)
a=x[0]
b=x[1]
c=x[2]
print(" ".join('%s' %id for id in x))
if a+b<c:
    print("No")
elif a*a+b*b<c*c:
    print("Obtuse")
elif a*a+b*b==c*c:
    print("Right")
else:
    print("Acute")
