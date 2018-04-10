def times_table(num):
    print(" <",num,"단 > ")
    for count in range(1, 10):
        print(num," * ",str(count)," = ",str(int(num)*count))

while True:
    try:
        num=input("숫자를 입력하세요. (-1: 종료, all: 구구단 전체 출력): ")
        if int(num) >= 2 and int(num)<=9:
            times_table(num)

        else:
            raise ValueError
    except ValueError:
        if num=='all':
            for num in range(2, 10):
                times_table(num)
        elif num=='-1':
            break
        else:
            print("숫자를 잘못 입력하셨습니다.")
