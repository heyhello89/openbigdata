# coding: cp949
student=0
a=[]

print("<<학생 시험 평가 프로그램>>")
while student<5:
    grade=input(str(student+1)+"번 학생 점수를 입력하세요:")
    student=student+1
    a.append([student,int(grade)])

print("*평가 결과")
for (student,grade) in a:
    if grade>=60:
        print("%d번 학생 %d점 합격입니다" %(student,grade))
    else:
        continue
#        print("%d번 학생 %d점 합격입니다" %(student,grade))
