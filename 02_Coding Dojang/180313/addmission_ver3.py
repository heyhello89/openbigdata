#coding: cp949
age=int(input("나이를 입력하세요. : "))
addmission=0
rank="노인"

while True:
    if age<0:
        age=int(input("나이를 다시 입력하세요. :"))
    else:
        if age<4 :
            addmission=0
            rank="유아"
        elif age<14 :
            addmission=2000
            rank="어린이"
        elif age<19 :
            addmission=3000
            rank="청소년"
        elif age<66 :
            addmission=5000
            rank="성인"
        else:
            addmission=0
        if addmission==0:
            print("귀하는",rank,"등급이며, 요금은 무료 입니다.")
        else:
            print("귀하는",rank,"등급이며, 요금은 ",addmission,"원 입니다.")
        break


pay=int(input("요금을 입력하세요. :"))
if pay<addmission:
    print(addmission-pay,"가 모자랍니다. 입력하신",pay,"를 반환합니다.")
elif pay==addmission:
    print("감사합니다. 티켓을 발행합니다.")
else:
    print("감사합니다. 티켓을 발행하고 거스름돈",pay-addmission,"를 반환합니다.")





