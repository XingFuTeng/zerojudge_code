for i in range(int(input())):
    a=sorted(list(map(int,input().split())))
    if a[0]+a[1]>a[2]:
        print("OK")
    else:
        print("Wrong!!")
                   
               
