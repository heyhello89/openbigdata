def sum_and_mul(a,b):
    return a+b,a*b

result = sum_and_mul(3,4)

print(result)

print("덧셈 연산 결과: "+str(result[0]))
if result[0] > 0:
    print("덧셈 분석 결과 양의 결과입니다.")
print("곱셈 연산 결과: "+str(result[1]))