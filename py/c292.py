A=[]
howb=int(input())
way=int(input())
for i in range(howb):
    x=list(map(int,input().split()))
    A.append(x)
print(A[howb//2][howb//2],end="")
for i in range(howb//2):
    for w in range(4):
        for m in range((i+1)*2):
            if (w==0 and way==0) or (w==3 and way==1) or (w==2 and way==2) or (w==1 and way==3):
                print(A[(howb//2)+i-m][(howb//2)-(i+1)],end="")  
            if (w==1 and way==0) or (w==0 and way==1) or (w==3 and way==2) or (w==2 and way==3):
                print(A[(howb//2)-(i+1)][(howb//2)-i+m],end="")
            if (w==2 and way==0) or (w==1 and way==1) or (w==0 and way==2) or (w==3 and way==3):
                print(A[(howb//2)-i+m][(howb//2)+(i+1)],end="")
            if (w==3 and way==0) or (w==2 and way==1) or (w==1 and way==2) or (w==0 and way==3):
                print(A[(howb//2)+(i+1)][(howb//2)+(i-m)],end="")
