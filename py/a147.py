while True:
    a=int(input())
    if a ==0:
        break
    for i in range(a-1):
        if (i+1)%7!=0:
            print(i+1,end=" ")
    print()
    
            
