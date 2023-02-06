a=int(input())
x=list(input())
w=[]
for i in range(len(x)):
    if x[i].isupper():
        w.append(1)
    else:
        w.append(0)
x=0
over=False
up=[False,0,0]
down=[False,0,0]
pr=0
pri=[]
for i in range(len(w)):
    #print(up,down)
    if up[1]==a:
        up[2]+=1
        up[1]=0
        up[0]=False
        down[0]=True
        pr+=a
    if down[1]==a:
        down[2]+=1
        down[1]=0
        down[0]=False
        up[0]=True
        pr+=a
    if up[0]==True:
        if w[i]==1:
            up[1]+=1
        else:
            up=[False,0,0]
            down=[False,1,0]
            over=False
            pri.append(pr)
            pr=0
    elif down[0]==True:
        if w[i]==0:
            down[1]+=1
        else:
            up=[False,1,0]
            down=[False,0,0]
            over=False
            if pr!=a:
                pri.append(pr)
            pr=0
    else:
        if w[i]==1:
            up[1]+=1
            up[0]=True
        if w[i]==0:
            down[1]+=1
            down[0]=True
if pri==[]:
    print(1)
else:
    print(max(pri))
