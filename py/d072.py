for i in range(int(input())):
    a=int(input())
    if a%400==0:
        print("Case %d: a leap year"%(i+1))
    elif a%100==0:
        print("Case %d: a normal year"%(i+1))
    elif a%4==0:
        print("Case %d: a leap year"%(i+1))
    else:
        print("Case %d: a normal year"%(i+1))
