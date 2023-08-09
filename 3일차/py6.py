a=float(input('키를 입력하세요:'))
b=float(input('몸무게를 입력하세요:'))
c=b/a**2
if c<18.5:
    print('저체중')
if c>18.5 and c<22.9:
    print('정상')
if c>23 and c<24.9:
    print('과체중')
if c>25 and c<29.9:
    print('비만')
if c>30:
    print('고도비만')