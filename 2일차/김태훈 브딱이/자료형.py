# a=0.00000001
# print(bool(a))

#hello="Hello World!"
#print(hello)
#print(hello[0])
#print(hello[3])
#print(hello[0:3])

#string_1='Hello World'
#string_2='안녕 세상아!'
#print(len(string_1))
#print(len(string_2))

#Print("12"+"32")

#a=10
#b="alpha"
#print(a/b)

#x=10
#y=10
#x+=1
#y*=2
#print(f"x={x},y={y}")

#print(4/3*3.14*3**3)

#x=int(input('숫자입력:'))
#y=int(input('숫자입력:'))
#print(f"x==y의 결과값:{x==y}")
#print(f"x!=y의 결과값:{x!=y}")
#print(f"x>y의 결과값:{x>y}")
#print(f"x<y의 결과값:{x<y}")
#print(f"x>=y의 결과값:{x>=y}")
#print(f"x<=y의 결과값:{x<=y}")

year=int(input())
if(year % 4 ==0 and year % 100 !=0 ) or year %400 == 0:
    print(f"{year}년은 윤년입니다.")
else:
    print(f"{year}은 윤년이 아닙니다.")