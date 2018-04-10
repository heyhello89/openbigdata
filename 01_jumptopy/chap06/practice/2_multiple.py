def print_num(ans):
    for i in ans:
        if i==ans[-1]:
            print(str(i)+" ",end="")
        else:
            print(str(i)+", ",end="")

def multiple(a, b):
    ans=[]
    for count in range(1, (int(a)//int(b))+1):
        result=int(b)*count
        ans.append(result)
    return ans

def set_mul(a, b, c):
    list_mul=[]
    list_mul.extend(multiple(a, b))
    list_mul.extend(multiple(a, c))
    set_mul=set(list_mul)
    mul=list(set_mul)
    return mul

def sum(mul):
    result=0
    for num in mul:
        result+=num
    print(result, end="")

input_num=input("범위, 첫 번째 수, 두 번째 수를 입력하세요. (종료: 프로그램 종료): ").split()

print("0 부터"+input_num[0],"이하의 범위를 선택하셨습니다. 이 중에서")
print(input_num[1]+"의 배수는 ", end="")
print_num(multiple(input_num[0], input_num[1]))
print("입니다.")

print(input_num[2]+"의 배수는 ", end="")
print_num(multiple(input_num[0], input_num[2]))
print("입니다.")

print(input_num[1]+"과 "+input_num[2]+"의 배수는 ", end="")
print_num(set_mul(input_num[0], input_num[1], input_num[2]))
print("입니다.")

print("따라서 0부터 "+input_num[0]+"이하의 범위내에서 "+input_num[1]+"과 "+input_num[2]+"배수의 총합은 ", end="")
sum(set_mul(input_num[0], input_num[1], input_num[2]))
print("입니다.")