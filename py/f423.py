x=int(input())
a=1
p=0
while True:
    p+=a
    a=a+2
    if x+2==a or x+1==a:
        break
print(p)
