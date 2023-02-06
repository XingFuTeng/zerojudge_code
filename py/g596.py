up=0
right=0
down=0
left=0
ispass=0
p1=0
a=list(map(int,input().split()))
x=[]
y=[]
n=0
for i in range(a[1]+2):
    y.append(-1000)
x.append(y)
y=[]
for i in range(a[0]):
    y.append(-1000)
    for j in range(a[1]):
        y.append(0)
    y.append(-1000)
    x.append(y)
    y=[]
for i in range(a[1]+2):
    y.append(-1000)
x.append(y)
y=[]
#print(x)
j=0
for i in range(a[2]):
    w=list(map(int,input().split()))
    w[0]+=1
    w[1]+=1
    print(w[0],w[1],w[2])
    if w[2]==0:
        if x[w[0]][w[1]]!=0:
            j=0
            up=0
            right=0
            down=0
            left=0
            ispass=0
            while True:
                if x[w[0]][w[1]+1+j]==1000:
                    up=1
                    break
                elif x[w[0]][w[1]+1+j]==-1000:
                    break
                j+=1
            j=0
            while True:
                if x[w[0]+1+j][w[1]]==1000:
                    right=1
                    break
                elif x[w[0]+1+j][w[1]]==-1000:
                    break
                j+=1
            j=0
            while True:
                if x[w[0]][w[1]-1-j]==1000:
                    down=1
                    break
                elif x[w[0]][w[1]-1-j]==-1000:
                    break
                j+=1
            j=0
            while True:
                if x[w[0]-1-j][w[1]]==1000:
                    left=1
                    break

                elif x[w[0]-1-j][w[1]]==-1000:
                    break
                j+=1
            j=0
            if up==1 and down==1:
                while x[w[0]][w[1]+1+j]!=1000:
                    x[w[0]][w[1]+1+j]=x[w[0]][w[1]+1+j]-1
                    j+=1
                j=0
                while x[w[0]][w[1]-1-j]!=1000:
                    x[w[0]][w[1]-1-j]=x[w[0]][w[1]-1-j]-1
                    j+=1
                j=0
            if right==1 and left==1:
                while x[w[0]+1+j][w[1]]!=1000:
                    x[w[0]+1+j][w[1]]=x[w[0]+1+j][w[1]]-1
                    j+=1
                j=0
                while x[w[0]-1-j][w[1]]!=1000:
                    x[w[0]-1-j][w[1]]=x[w[0]-1-j][w[1]]-1
                    j+=1
                j=0
        x[w[0]][w[1]]=1000
        j=0
        up=0
        right=0
        down=0
        left=0
        ispass=0
        while True:
            if up!=-1000:
                if x[w[0]][w[1]+1+j]==1000:
                    for i in range(j):
                       x[w[0]][w[1]+i+1]+=1
                    up=-1000
                elif x[w[0]][w[1]+1+j]==-1000:
                    up=-1000
            if right!=-1000:
                if x[w[0]+1+j][w[1]]==1000:
                    for i in range(j):
                       x[w[0]+i+1][w[1]]+=1
                    right=-1000
                elif x[w[0]+1+j][w[1]]==-1000:
                    right=-1000
            if down!=-1000:
                if x[w[0]][w[1]-1-j]==1000:
                    for i in range(j):
                       x[w[0]][w[1]-1-i]+=1
                    down=-1000
                elif x[w[0]][w[1]-1-j]==-1000:
                    down=-1000
            if left!=-1000:
                if x[w[0]-1-j][w[1]]==1000:
                    for i in range(j):
                       x[w[0]-1-i][w[1]]+=1
                    left=-1000
                elif x[w[0]-1-j][w[1]]==-1000:
                    left=-1000
            j+=1
            if up+down+right+left==-4000:
                break
            #for i in range(len(x)):
                #print(x[i])
    if w[2]==1:
        x[w[0]][w[1]]=0
        j=0
        j=0
        up=0
        right=0
        down=0
        left=0
        ispass=0
        j=0
        while True:
            if up!=-1000:
                if x[w[0]][w[1]+1+j]==1000:
                    for i in range(j):
                        x[w[0]][w[1]+i+1]=x[w[0]][w[1]+i+1]-1
                    up=-1000
                    ispass+=1
                elif x[w[0]][w[1]+1+j]==-1000:
                    up=-1000
                    ispass+=1
            if right!=-1000:
                if x[w[0]+1+j][w[1]]==1000:
                    for i in range(j):
                        x[w[0]+1+i][w[1]]=x[w[0]+1+i][w[1]]-1
                    right=-1000
                    ispass+=1
                elif x[w[0]+1+j][w[1]]==-1000:
                    right=-1000
                    ispass+=1
            if down!=-1000:
                if x[w[0]][w[1]-1-j]==1000:
                   for i in range(j):
                       x[w[0]][w[1]-1-i]=x[w[0]][w[1]-1-i]-1
                       down=-1000
                       ispass+=1
                elif x[w[0]][w[1]-1-j]==-1000:
                    down=-1000
                    ispass+=1
            if left!=-1000:
                if x[w[0]-1-j][w[1]]==1000:
                   for i in range(j):
                       x[w[0]-1-i][w[1]]=x[w[0]-1-i][w[1]]-1
                       left=-1000
                       ispass+=1
                elif x[w[0]-1-j][w[1]]==-1000:
                    left=-1000
                    ispass+=1
            j+=1
            if ispass==4:
                break
            #for i in range(len(x)):
                #print(x[i])
    for i in range(a[0]+2):
        for j in range(a[1]+2):
            if x[i][j]>0:
                n+=1
    for i in range(len(x)):
        print(x[i])
    print("帥氣")
    if n>p1:
        p1=n
    n=0
n=0
for i in range(a[0]+2):
    for j in range(a[1]+2):
        if x[i][j]>0:
            n+=1
print(p1)
print(n)
#34 1 7
#29 0 0
#24 0 0
#13 0 0
#25 0 0
#22 0 0
#17 0 0
#13 0 1
                
                
        
