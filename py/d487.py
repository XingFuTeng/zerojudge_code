w=[1,1,2,6,24,120,720,5040,40320,362880,3628800]
try:
    while True:
        a=int(input())
        if a ==0:
            print("0! = 1 = 1")
        else:
            print("%d! = %d "%(a,a),end="")
            for i in range(a-1):
                print("* %d "%(a-i-1),end="")
            print("= %d"%w[a])
except EOFError:
    pass
