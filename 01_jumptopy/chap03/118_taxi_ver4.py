# coding: cp949
#pocket = ['paper','cellphone','money']
#pocket = ['paper','cellphone']
pocket = []

item=input("포켓에 아이템을 챙기세요: ")
pocket.append(item)

if 'card' in pocket:
    print("신용카드로 택시를 탈 것을 추천합니다.")
elif 'money' in pocket:
    print("현금 이용시 영수증을 꼭 챙기세요.")
elif 'cellphone' in pocket:
    print("스마트폰에 교통카드 기능이 있는지 확인하세요.")
else:
    print("걸어 가라")
