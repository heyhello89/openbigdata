# coding: cp949
food={"짜장면":"중식","비빔밥":"한식","짬뽕":"중식","불고기":"한식","스파게티":"양식","초밥":"일식","피자":"양식","햄버거":"양식"}
print("Step1] Printing the raw type of dictionaty,'food'")
print(food)

print("\nStep2] Printing the key lists using food.keys() function")
print(food.keys())

print("\nStep3] Printing the values lists using food.values() function")
print(food.values())

print("\nStep4] Trying to search character of '불고기' in the food dictionary")
for food_key in food.keys():
	print(food_key)
	if food_key == '불고기':
            print("\nI found 불고기! Now, I will tell you about that.")
            print("That is a "+food['불고기']+" food")
#                print("He is a "+food['불고기']+" food")
            break

print("\nProgram End")
