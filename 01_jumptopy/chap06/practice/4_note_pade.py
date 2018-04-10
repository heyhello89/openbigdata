import sys

mode=sys.argv[1]
string=sys.argv[2]

try:
    if mode=='-a':
        f=open('memo.txt', 'a')
        f.write(string+"\n")
        f.close()
    elif mode=='-au':
        f=open('memo.txt', 'a')
        f.write(string.upper()+"\n")
        f.close()
    elif mode=='-v':
        f=open('memo.txt','r')
        print(f.read())
        f.close()
except FileNotFoundError:
    type=input("아래중 선택하세요.\n1. 새로 생성하시겠습니까?\n2. 파일 경로를 입력하겠습니다.\n -- :")
    if type=='1':
        f=open('memo.txt','w')
        f.write(string+"\n")
        f.close()
    elif type=='2':
        path=input("경로를 입력하세요. : ")
        f.open(path, 'a')
        f.write(string+"\n")
        f.close()