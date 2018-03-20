# coding: cp949
print("<<구구단 출력 프로그램 ver1>>")
a=input("단 수를 입력하세요: ")
for i in range(2,10):
    if i==int(a):
        print (str(i)+"단")
        for j in range(1,10):
            print("%d*%d=%d" %(i,j,i*j))
