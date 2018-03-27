class Restaurant:

    def __init__(self, input_name):
        self.restaurant_name = input_name.split()[0]
        self.cuisine_type = input_name.split()[1]

    def describe_restaurant(self):
        print("저희 레스토랑 명칭은 %s이고 %s 전문점입니다."%(self.restaurant_name, self.cuisine_type))

    def open_restaurant(self):
        print("저희 %s 레스토랑 오픈했습니다. 어서오세요."%(self.restaurant_name))

    def __del__(self):
        print(self.restaurant_name + " 레스토랑 문 닫았습니다.")

res1=Restaurant(input_name = input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분): "))
res1.describe_restaurant()
res1.open_restaurant()

res2=Restaurant(input_name = input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분): "))
res2.describe_restaurant()
res2.open_restaurant()

res3=Restaurant(input_name = input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분): "))
res3.describe_restaurant()
res3.open_restaurant()

print("저녁 10시가 되었습니다.")
