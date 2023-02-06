while True:
    try:
        m,n = input().split()
        m = int(m)
        n = int(n)
        matrix = []
        for i in range(m):
            matrix.append(input().split())

        for i in range(n):
            for j in range(m):
                print(matrix[j][i],end = " ")
            print()
    except:
            break
