try:
    while True:
        a=list(map(int,input().split()))
        if (sum(a)-a[0])/a[0]>59:
            print("no")
        else:
            print("yes")
except EOFError:
    pass
