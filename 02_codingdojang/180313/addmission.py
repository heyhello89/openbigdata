#coding: cp949
age=int(input("���̸� �Է��ϼ���. : "))
addmission=0
if age<0 :
    print("���̸� �߸� �Է��ϼ̽��ϴ�. ")
    continue
elif age<4 :
    addmission=0
elif age<14 :
    addmission=2000
elif age<19 :
    addmission=3000
elif age<66 :
    addmission=5000
else:
    addmission=0

if addmission==0:
    print("����� ���� �Դϴ�.")
else:
    print("����� ", addmission,"�� �Դϴ�.")
