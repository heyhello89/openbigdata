def insert_birth():
    birth = input("생년월일을 입력하세요 (예:801212):")
    print(name + "님 환영합니다. 아래 내용을 입력하셨습니다.\n" + name + " " + birth)
    with open('방명록.txt', 'a', encoding='UTF8') as f:
        f.writelines(name + " " + birth + "\n")

def search_visitor(name):
    for i in visitor:
        if name==i[:3]:
            print(name+"님 다시 방문해 주셔서 감사합니다. 즐거운 시간되세요.")
            return True
    return False

name=input("이름을 입력하세요.: ")
f=open('방명록.txt', 'r', encoding='UTF8')

visitor = f.readlines()

if not search_visitor(name):
    insert_birth()