try:
    while True:
        input()
        a=map(str,sorted(list(map(int,input().split()))))
        print(' '.join(a))
except EOFError:
    pass
