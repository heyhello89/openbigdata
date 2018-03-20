#coding: cp949

sum=0
while True:
    X=int(input("X를 입력하세요 :"))
    Y=int(input("Y를 입력하세요 :"))
    Z=int(input("Z를 입력하세요 :"))
    if X==0 or Y==0 or Z==0:
        print("프로그램을 종료합니다.")
        break

    for i in range(1,Z):
        if i%X==0 or i%Y==0:
            sum+=i
    print("총합:",sum)

