word = input('단어를 입력해주세요')


count = 0
for char in word:
    if char in ['a','e','i','o','u']:
        count +=1

print("모음의 개수:",count)
    