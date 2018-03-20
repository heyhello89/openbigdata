#coding: cp949
age=int(input("나이를 입력하세요. : "))
addmission=0
if age<0 :
    print("나이를 잘못 입력하셨습니다. ")
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
    print("요금은 무료 입니다.")
else:
    print("요금은 ", addmission,"원 입니다.")
