# coding: cp949
print("<<������ ��� ���α׷� ver1>>")
a=input("�� ���� �Է��ϼ���: ")
for i in range(2,10):
    if i==int(a):
        print (str(i)+"��")
        for j in range(1,10):
            print("%d*%d=%d" %(i,j,i*j))
