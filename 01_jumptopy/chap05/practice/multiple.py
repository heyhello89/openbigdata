while True:
    num=int(input("양수를 입력하세요. (종료시 -1): "))
    if num==-1:
        break
    else:
        if num%10==0:
            print("%s는 10의 배수입니다."%num)
        else:
            print("%s는 10의 배수가 아닙니다."%num)
