for i in range(int(input())):
    x=int(input())
    if x%2==0:
        print(((x//2)**2)%998244353)
    elif x==1:
        print(1)
    else:
        print(((x//2)*(x//2+1))%998244353)
