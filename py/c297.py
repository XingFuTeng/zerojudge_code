al=[]
for i in range(9):
    a=list(input().split(" "))
    al.append(a)
t=int(input())
sco=0
x=[0,0,0]
out=0
j=0
tf=False
while True:
    j+=1
    for i in range(9):
        if out==t:
            tf=True
            print(sco)
            break
        w=al[i][j]
        if w=="1B":
            x.append(1)
            if x[0]==1:
                sco+=1
            x[:1]=[]
        elif w=="2B":
            x.append(1)
            x.append(0)
            if x[0]==1:
                sco+=1
            if x[1]==1:
                sco+=1
            x[:2]=[]
        elif w=="3B":
            x.append(1)
            x.append(0)
            x.append(0)
            if x[0]==1:
                sco+=1
            if x[1]==1:
                sco+=1
            if x[2]==1:
                sco+=1
            x[:3]=[]
        elif w=="HR":
            sco+=(sum(x)+1)
            x=[0,0,0]
        elif w=="FO" or w=="SO" or w=="GO":
            out+=1
            if out%3==0:
                x=[0,0,0]
    if tf==True:
        break
