from itertools import accumulate
import sys
try:
  while True:
    ls=[]
    a,b=map(int,sys.stdin.readline().split())
    for i in range(a):
        x=list(map(int,sys.stdin.readline().split()))
        ls.append(x)
    for i in range(a):
        x=[0]+list(accumulate(ls[i]))
        ls[i]=x
    for i in range(b):
        p=0
        x1,y1,x2,y2=map(int,sys.stdin.readline().split())
        for m in range(y2-y1+1):
            p+=ls[y1+m-1][x2]-ls[y1+m-1][x1-1]
        print(p)
except EOFError:
    pass
