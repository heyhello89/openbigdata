# coding: cp949
student=0
a=[]

print("<<�л� ���� �� ���α׷�>>")
while student<5:
    grade=input(str(student+1)+"�� �л� ������ �Է��ϼ���:")
    student=student+1
    a.append([student,int(grade)])

print("*�� ���")
for (student,grade) in a:
    if grade>=60:
        print("%d�� �л� %d�� �հ��Դϴ�" %(student,grade))
    else:
        continue
#        print("%d�� �л� %d�� �հ��Դϴ�" %(student,grade))
