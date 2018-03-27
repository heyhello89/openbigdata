in_no=int(input("안녕하세요. 저희 가게에 방문해 주셔서 감사합니다.\n1. 주문\n2. 종료\n입력: "))

order = []

def input_ingredient():
    while True:
        a=input("안녕하세요. 원하시는 재료를 입력하세요: ")
        if a=='종료':
            break
        order.append(a)

def make_sandwich(order):
    print("샌드위치를 만들겠습니다.")
    for i in order:
        print(i,"추가합니다.")
    print("여기 주문하신 샌드위치 만들었습니다. 맛있게 드세요.")

if in_no==1:
    input_ingredient()
    make_sandwich(order)


