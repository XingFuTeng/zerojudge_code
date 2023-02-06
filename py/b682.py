x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
a=x1*60+y1
b=x2*60+y2
if a>b:
    b+=1440
w=(a-b)
print((b-a)//60,end=" ")
print((b-a)%60)
