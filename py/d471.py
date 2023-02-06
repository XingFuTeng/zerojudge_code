try:
    while True:
        a=int(input())
        for i in range(2**a):
            print(str(bin(i)[2:].zfill(a)))
except EOFError:
    pass
