num1, num2 = input("두개의 숫자를 입력하세요.").split()
is_calculate=True

try:
    f = open('나없는 파일','r')
    result = int(num1)/int(num2)

except FileNotFoundError:
    print("파일이존재하지 않습니다.")
    print("System Error Message"+str(e))
    is_calculate=False

except ZeroDivisionError:
    print("연산을 할 수 없습니다.")
    print("System Error Message: "+str(e))
    is_calculate=False

if is_calculate:
    print("%s/%s=%s"%(num1,num2,result))