try:
    while True:
        a=float(input())
        b=abs(a)
        print("|%.4f|=%.4f"%(a,b))
except EOFError:
    pass
