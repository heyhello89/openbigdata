while True:
    age=int(input("나이를 입력하세요. (음수를 입력하면 종료됩니다): "))
    if age >= 0 and age < 3:
        print("입장권은 무료입니다.")
    elif age >= 3 and age <= 12:
        print("입장권은 10달러입니다.")
    elif age > 12:
        print("입장권은 15달러입니다.")
    else:
        print("프로그램이 종료됩니다.")
        break