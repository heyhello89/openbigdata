survey=[]
name=[]
count=0

while True:
    survey_input=input("프로그래밍이 왜 좋으세요? (종료 입력시 프로그램 종료): ")
    if survey_input=="종료":
        with open('poll.txt','w',encoding='utf8') as main:
            for num in range(0,count):
                main.write("["+name[num]+"] "+survey[num]+"\n")
        break

    else:
        survey.append(survey_input)
        name_input=input("이름을 입력해 주세요.: ")
        name.append(name_input)
        print("설문에 응답해 주셔서 감사합니다.")
        count+=1

print(survey, name)
