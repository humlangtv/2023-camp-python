a=int(input("숫자를 입력하세요:"))
for i in range(1,a+1):
    if i==3 or i==6 or i==9:
        print("-",end=" ")
    else:
        print(i,end=" ")