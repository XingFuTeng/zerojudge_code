try:
    while True:
        x=0
        a,b=map(int,input().split())
        al=0
        while True:
            al=al+a+x
            if al>b:
                break
            x+=1
        print(x+1)
except EOFError:
    pass
            
            
