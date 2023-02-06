try:
    while True:
        pr=0
        x=0
        b=list(input())
        for i in range(len(b)):
            if b[i]=="y":
                pr+=abs((i-x))
                x+=3
        print(pr)
except EOFError:
    pass
