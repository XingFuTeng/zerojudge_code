for i in range(int(input())):
    a=list(map(int,input().split()))
    print("%.2f"%((sum(a)-a[0])/(len(a)-1)))
