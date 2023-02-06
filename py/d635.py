while True:
    a=input()
    if a=="-1":
        print(-1)
        break
    b=list(map(int,input()))
    print(b[0]*64+b[1]*8+b[2])
