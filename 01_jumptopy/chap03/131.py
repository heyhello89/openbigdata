# coding: cp949
student_name_lists=[
        ('��','����'),
        ('��','���'),
        ('��','����'),
        ('��','ȿ��'),
        ('��','����'),
        ]
print(student_name_lists)

for (i,j) in student_name_lists:
    print(i+j)

Fname=input("First_name�� �Է��ϼ���: ")
is_found_flag=False
for (First_name,Last_name) in student_name_lists:
    if First_name==Fname:
        if is_found_flag==False:
            print("<<�˻� ���>>")
            is_found_flag=True
        print(First_name+Last_name)
