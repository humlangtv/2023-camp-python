a=int(input('삼강형의 크기'))
for i in range(a,0,-1):
    for j in range(i):
        print("*",end='')
    print()