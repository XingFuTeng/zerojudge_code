al=0
bl=0
pl=0
a,b=map(int,input().split(" "))
for i in range(int(input())):
    x=list(map(int,input().split()))
    for w in range(len(x)):
        if x[w]==0:
            break
        if abs(x[w])==a:
            if x[w]>0:
                al=al+1
            else:
                al=al-1
        if abs(x[w])==b:
            if x[w]>0:
                bl=bl+1
            else:
                bl=bl-1
    if al>0 and bl>0:
        pl+=1
    #print(al)
    #print(bl)
    al=0
    bl=0
print(pl)
