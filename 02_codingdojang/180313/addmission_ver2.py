#coding: cp949
age=int(input("���̸� �Է��ϼ���. : "))
addmission=0
rank="����"

while True:
    if age<0:
        age=int(input("���̸� �ٽ� �Է��ϼ���. :"))
    else:
        if age<4 :
            addmission=0
            rank="����"
        elif age<14 :
            addmission=2000
            rank="���"
        elif age<19 :
            addmission=3000
            rank="û�ҳ�"
        elif age<66 :
            addmission=5000
            rank="����"
        else:
            addmission=0
        if addmission==0:
            print("���ϴ�",rank,"����̸�, ����� ���� �Դϴ�.")
        else:
            print("���ϴ�",rank,"����̸�, ����� ",addmission,"�� �Դϴ�.")
        break




