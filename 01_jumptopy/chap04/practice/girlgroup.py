f=open('연습생.txt', 'r', encoding='UTF8')
candidate_list = f.readlines()

def show_candidates(candidate_list):
    for i in candidate_list:
        print(i.strip())

def make_idol(candidate_list):
    for i in candidate_list:
        print("신예 아이돌 "+i.strip()+" 인기 급상승")

def make_world_star(candidate_list):
    for i in candidate_list:
        print("아이돌 "+i.strip()+" 월드스타 등극")

show_candidates(candidate_list)
make_idol(candidate_list)
make_world_star(candidate_list)