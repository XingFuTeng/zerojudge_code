try:
    while True:
        a=int(input())
        x=[1000,500,100,50,10,5,1]
        print("%d ="%a,end=" ")        
        for i in range(len(x)):
            w=a//x[i]
            if w>0:
                print("%d*%d"%(x[i],w),end=" ")
                a=a-(x[i]*w)
                if a!=0:
                    print("+",end=" ")
        print()
except EOFError:
    pass
        
