#coding: cp949

m=int(input("�ѰǼ� : "))
n=int(input("�������� �Խù� �� : "))

result=int(m/n)
if m%n>0:
    result=result+1
print("�� ������ �� :",result)
