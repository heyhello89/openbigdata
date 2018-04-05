while True:
    num=input("세 개의 양수를 입력하세요. (종료시 -1): ")

    if num == "-1":
        break
    else:
        if int(num.split()[2])%int(num.split()[0])==0 and int(num.split()[2])%int(num.split()[1])==0:
            print("%s는 %s와 %s의 공배수입니다."%(num.split()[2],num.split()[0],num.split()[1]))
        else:
            print("%s는 %s와 %s의 공배수가 아닙니다."%(num.split()[2],num.split()[0],num.split()[1]))

