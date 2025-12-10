a = int(input("첫 번째 점수? "))
b = int(input("두 번째 점수? "))
c = int(input("세 번째 점수? "))
avg = (a + b + c) / 3
print("평균 점수는", avg)
if avg>=80:
    print('합격')
else:
    print('불합격')