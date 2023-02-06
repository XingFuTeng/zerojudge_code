try:
    while True:
        input()
        a=sorted(list(map(int,input().split())))
        for i in range(len(a)):
            print(a[i],end=" ")
        print()
except EOFError:
    pass
        
