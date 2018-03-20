# coding: cp949
student_name_lists=[
        ('유','영재'),
        ('문','희식'),
        ('김','광훈'),
        ('이','효진'),
        ('문','재인'),
        ]
print(student_name_lists)

for (i,j) in student_name_lists:
    print(i+j)

Fname=input("First_name을 입력하세요: ")
is_found_flag=False
for (First_name,Last_name) in student_name_lists:
    if First_name==Fname:
        if is_found_flag==False:
            print("<<검색 결과>>")
            is_found_flag=True
        print(First_name+Last_name)
