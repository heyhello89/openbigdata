def write_content(way, r):
    survey=[]
    name=[]
    count=0
    while True:
        survey_input=input("프로그래밍이 왜 좋으세요? (종료 입력시 프로그램 종료): ")
        if survey_input=="종료":
            with open(way,r,encoding='utf8') as main:
                for num in range(0,count):
                    main.write("["+name[num]+"] "+survey[num]+"\n")
            break

        else:
            survey.append(survey_input)
            name_input=input("이름을 입력해 주세요.: ")
            name.append(name_input)
            print("설문에 응답해 주셔서 감사합니다.")
            count+=1

def read_content(way):
    main = open(way,'r',encoding='utf8')
    print(main.read())

try:
    read_content('poll.txt')
except FileNotFoundError:
    error=int(input("기존 poll.txt 파일을 찾을 수 없습니다. 아래 중 선택하세요. \n1.종료 2.새로운 파일 생성 3.변경된 파일 경로 입력: "))
    if error==1:
        print("프로그램이 종료됩니다.")

    elif error==2:
        write_content(way='poll.txt', r='w')
        print(read_content('poll.txt'))

    elif error==3:
        way=input("변경된 파일 경로를 입력하세요. : ")
        with open(way,'r',encoding='utf8') as main:
            print(main.read())
        write_content(way, r='a')
        print(read_content(way))