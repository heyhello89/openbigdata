# coding: cp949

prompt="""
1. 추가
2. 삭제
3. 목록
4. 종료

숫자를 입력하세요: """

number=0

while number!=4:
    number=int(input(prompt))
    if number==1:
        print("'1. 추가' 메뉴를 선택하셨습니다.")
    elif number==2:
        print("'2. 삭제' 메뉴를 선택하셨습니다.")
    elif number==3:
        print("'3. 목록' 메뉴를 선택하셨습니다.")
    elif number==4:
        print("'4. 종료' 메뉴를 선택하셨습니다.")


