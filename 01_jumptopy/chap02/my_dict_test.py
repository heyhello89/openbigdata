# coding: cp949
food={"¥���":"�߽�","�����":"�ѽ�","«��":"�߽�","�Ұ��":"�ѽ�","���İ�Ƽ":"���","�ʹ�":"�Ͻ�","����":"���","�ܹ���":"���"}
print("Step1] Printing the raw type of dictionaty,'food'")
print(food)

print("\nStep2] Printing the key lists using food.keys() function")
print(food.keys())

print("\nStep3] Printing the values lists using food.values() function")
print(food.values())

print("\nStep4] Trying to search character of '�Ұ��' in the food dictionary")
for food_key in food.keys():
	print(food_key)
	if food_key == '�Ұ��':
            print("\nI found �Ұ��! Now, I will tell you about that.")
            print("That is a "+food['�Ұ��']+" food")
#                print("He is a "+food['�Ұ��']+" food")
            break

print("\nProgram End")
