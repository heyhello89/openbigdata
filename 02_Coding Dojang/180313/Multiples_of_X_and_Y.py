#coding: cp949

sum=0
while True:
    X=int(input("X�� �Է��ϼ��� :"))
    Y=int(input("Y�� �Է��ϼ��� :"))
    Z=int(input("Z�� �Է��ϼ��� :"))
    if X==0 or Y==0 or Z==0:
        print("���α׷��� �����մϴ�.")
        break

    for i in range(1,Z):
        if i%X==0 or i%Y==0:
            sum+=i
    print("����:",sum)

