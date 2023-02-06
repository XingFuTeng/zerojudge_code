d=1
while True:
    a=input()
    if a == "#":
        break
    elif a=="HELLO":
        print("Case ",end="")
        print(d,end="")
        print(": ENGLISH")
    elif a=="HOLA":
        print("Case ",end="")
        print(d,end="")
        print(": SPANISH")
    elif a=="HALLO":
        print("Case ",end="")
        print(d,end="")
        print(": GERMAN")
    elif a=="BONJOUR":
        print("Case ",end="")
        print(d,end="")
        print(": FRENCH")
    elif a=="CIAO":
        print("Case ",end="")
        print(d,end="")
        print(": ITALIAN")
    elif a=="ZDRAVSTVUJTE":
        print("Case ",end="")
        print(d,end="")
        print(": RUSSIAN")
    else:
        print("Case ",end="")
        print(d,end="")
        print(": UNKNOWN")
    d+=1
