def my_sum(num1,num2):
    print("덧셈 연산")
    internal_result = num1 + num2
    if internal_result > 0:
        print("연산 결과가 양수로 분석됩니다.")
    elif internal_result ==0:
        print("연산 결과가 양수로 분석됩니다.")
    else:
        return num1+num2

result=my_sum(1,2)

print("최종 연산 결과: ",result)
print("계산기 ver1.0 종료")