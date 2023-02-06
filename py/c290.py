a=input()
b=list(map(int,a))
print(abs(sum(b[::2])-sum(b[1::2])))
