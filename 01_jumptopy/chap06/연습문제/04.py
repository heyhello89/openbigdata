import sys

def f_open(text):
    f = open('memo.txt', 'a', encoding='UTF-8')
    f.write(text + "\n")
    f.close()

option=sys.argv[1]
text=sys.argv[2]
try:
    if option=='-a':
        f=open('memo.txt','r',encoding='UTF-8')
        f_open(text)

    elif option=='-au':
        text=text.upper()
        f_open(text)

    elif option=='-v':
        f = open('memo.txt', 'r', encoding='UTF-8')
        text_list=f.read()
        print(text_list)
        f.close()

except FileNotFoundError:
    if option=='-a':
        select = int(input("아래중 선택하세요.\n1. 새로 생성하시겠습니까?"
                           "\n2. 파일 경로를 입력하겠습니까?\n 입력 : "))
        if select==1:
            f_open(text)
        elif select==2:
            in_msg=input("경로 : ")
            f = open('%s'%in_msg, 'a', encoding='UTF-8')
            f.write(text+"\n")
            f.close()

    elif option=='-v':
        select = int(input("아래중 선택하세요.\n1. 종료하시겠습니까?"
                           "\n2. 파일 경로를 입력하세요.\n 입력 : "))
        if select == 1:
            exit()
        elif select==2:
            in_msg = input("경로 : ")
            f = open('%s' % in_msg, 'r', encoding='UTF-8')
            text_list = f.read()
            print(text_list)
            f.close()