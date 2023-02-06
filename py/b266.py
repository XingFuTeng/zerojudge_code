try:
   while True: 
        B=[]
        a=list(map(int,input().split(" ")))
        for i in range(a[0]):
            c=list(map(int,input().split(" ")))
            B.append(c)
        x=list(map(int,input().split(" ")))
        #print(B)
        for j in range(a[2]):
            #print(B)
            if x[-j-1]==0:
                new=[]
                for i in range(len(B[0])):
                    c=[]
                    for w in range(len(B)):
                        c.append(B[w][-i-1])
                        #print(B[w][-i-1]) 
                    #print(c)
                    new.append(c)
                    
                    
                B=new
            if x[-j-1]==1:
                new=[]
                for i in range(len(B)):
                    c=[]
                    c=B[-i-1]
                    new.append(c)
                B=new
        print(len(B),end=" ")
        print(len(B[0]))
        for j in range(len(B)):
            for i in range(len(B[0])):
                if i==len(B[0])-1:
                    print(B[j][i])
                else:
                    print(B[j][i],end=" ")
            #print()
except EOFError:
    pass
        
