def gugudan(num):
    print("**** %d단 ****"%num)
    for i in range(1,10):
        print("%d * %d = %d"%(num,i,num*i))

try :
    in_num=input("숫자를 입력하세요.(-1:종료, all: 구구단 전체 출력) : ")
    in_num=int(in_num)
    if in_num>0:
        gugudan(in_num)

    else :
        raise ValueError

except ValueError :
    if in_num=='all':
        for i in range(2,10):
            gugudan(i)
    else :
        print("정수를 입력하세요.")