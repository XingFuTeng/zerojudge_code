a=list(map(int,input().split()))
if a[0]==a[1] and a[0]==a[2]:
    print(3,end=" ")
    print(a[0])
elif a[0]==a[1] or a[2]==a[1] or a[2]==a[0]:
    print(2,end=" ")
    print(max(a),end=" ")
    print(min(a))
else:
    print(1,end=" ")
    print(max(a),end=" ")
    print(sum(a)-max(a)-min(a),end=" ")
    print(min(a))
