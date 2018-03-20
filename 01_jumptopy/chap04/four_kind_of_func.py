def my_sum1(num1,num2):
    print("덧셈 연산 - 함수 타입1")
    internal_result = num1 + num2
    if internal_result > 0:
        print("연산 결과가 +로 분석됩니다.")
    else:
        print("연산 결과가 -로 분석됩니다.")
    return num1 + num2

def my_sum2(num1, num2):
    print("덧셈 연산 - 함수 타입1")
    internal_result = num1 + num2
    if internal_result > 0:
        print("연산 결과가 +로 분석됩니다.")
    else:
        print("연산 결과가 -로 분석됩니다.")
    print("my_sum2() 연산 결과: "+ str(internal_result))

def my_sum3():
    print("덧셈 연산 - 함수 타입1")
    internal_result = 1 + 2
    if internal_result > 0:
        print("연산 결과가 +로 분석됩니다.")
    else:
        print("연산 결과가 -로 분석됩니다.")
    return internal_result

def my_sum4():
    print("덧셈 연산 - 함수 타입1")
    internal_result = 1 + 2
    if internal_result > 0:
        print("연산 결과가 +로 분석됩니다.")
    else:
        print("연산 결과가 -로 분석됩니다.")
    print("my_sum4() 연산 결과: "+str(internal_result))

result = my_sum1(1,2)
print("my_sum1() 연산 결과: "+ str(result))

my_sum2(1,2)

print("my_sum3() 연산 결과: "+str(my_sum3()))

my_sum4()