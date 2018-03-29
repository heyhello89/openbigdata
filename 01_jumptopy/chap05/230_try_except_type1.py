num1, num2 = input("두개의 숫자를 입력하세요.").split()
is_calculate=True

try:
    result = int(num1)/int(num2)
except:
    print("연산을 할 수 없습니다.")
    is_calculate=False

if is_calculate:
    print("%s/%s=%s"%(num1,num2,result))