class Restaurant:
    number_served=0
    def __init__(self, input_name):
        self.restaurant_name = input_name.split()[0]
        self.cuisine_type = input_name.split()[1]

    def describe_restaurant(self):
        print("저희 레스토랑 명칭은 %s이고 %s 전문점입니다."%(self.restaurant_name, self.cuisine_type))


    def open_restaurant(self):
        print("저희 %s 레스토랑 오픈했습니다."%(self.restaurant_name))

    def reset_number_served(self):
        self.number_served=0
        print("손님 카운팅을 0 으로 초기화 하였습니다.")

    def increment_number_served(self, number):
        self.number_served+=int(number)
        print("손님 "+number+"명 들어오셨습니다. 자리를 안내해 드리겠습니다.")

    def check_customer_number(self):
        print("지금까지 총 "+str(self.number_served)+"명 손님이 오셨습니다.")

    def close_restaurant(self):
        print("%s 레스토랑 문 닫습니다."%(self.restaurant_name))


pey=Restaurant(input_name = input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분): "))
pey.describe_restaurant()
input_open=input("레스토랑을 오픈하시겠습니까? (y/n) : ")
if input_open=='y':
    pey.open_restaurant()
    while True:
        number = input("어서오세요. 몇명이십니까?(초기화:0, 종료:-1, 누적고객 확인:p) : ")
        if number=='0':
            pey.reset_number_served()
        elif number=='-1':
            pey.close_restaurant()
            break
        elif number=='p':
            pey.check_customer_number()
        else:
            pey.increment_number_served(number)
else:
    pey.close_restaurant()