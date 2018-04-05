def sum(a, b):
    return print(a+b)

while True:
    num=input("안녕하세요 두 수를 입력하세요. (종료: 프로그램 종료) : ")
    if num=="종료":
        break
    try:
        a=int(num.split()[0])
    except ValueError:
        a=num.split()[0]
        a=int(input("죄송합니다. 첫번째 입력이 [%s]입니다. 숫자를 입력하세요. : "%a))
    try:
        b=int(num.split()[1])
    except ValueError:
        b=num.split()[1]
        b=int(input("죄송합니다. 두번째 입력이 [%s]입니다. 숫자를 입력하세요. : "%b))
    sum(a, b)



