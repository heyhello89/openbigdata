import json
from collections import OrderedDict
import re

def load_json():
    global get_information
    with open('ITT_Student.json','r',encoding='utf8') as selection:
        get_information=json.load(selection)
    return get_information

def search_word(search, key):
    load_json()
    global get_word
    get_word=[]
    for num in range(0, len(get_information)):
        for a in range(0,len(get_information[num][key])):
            for b in range(0,len(get_information[num][key])+1):
                if str(get_information[num][key][a:b])==search:
                    get_word.append(get_information[num][key])
                    print(get_word)
    return get_word

def print_result(get_word, key):
    if len(get_word)==1:
        for num in range(len(get_information)):
            if get_information[num][key]==get_word[0]):
                print("* 이름: %s"%get_information[num]['student_ID'])
                print("* 나이: %s"%get_information[num]['student_age'])
                print("* 주소: %s"%get_information[num]['address'])
                print("* 수강 정보")
                print(" + 과거 수강 횟수: %s"%get_information[num]['num_of_course_learned'])
                print(" + 현재 수강 과목: %s"%get_information[num]['learning_course_info'])
                print("  강의 코드: %s"%get_information[num]['course_code'])
                print("  강의명: %s"%get_information[num]['course_name'])
                print("  강사: %s"%get_information[num]['teacher'])
                print("  개강일: %s"%get_information[num]['open_date'])
                print("  종료일: %s"%get_information[num]['close_date'])

def insert_information():
    global file_data
    file_data = OrderedDict()
    get_infomation=load_json()
    count=len(get_infomation)
    file_data['student_ID'] = ("ITT{0:0>3}".format(count+1))
    file_data['student_name'] = input("이름 (예: 홍길동): ")
    file_data['student_age'] = input("나이 (예: 29): ")
    file_data['address'] = input("주소 (예: 대구광역시 동구 아양로 135): ")
    file_data['num_of_course_learned'] = input("과거 수강 횟수 ( 예: 1): ")
    now_learn=input("현재 수강하는 과목이 있습니까? (예: y/n): ")
    learning_course_info=[]
    while True:
        if now_learn=='y':
            course_code=input("강의코드 (예: IB171106, OB0104 ..): ")
            course_name=input("강의명 (예: IOT 빅데이터 실무반): ")
            teacher=input("강사 (예: 이현구): ")
            open_date=input("개강일 (예: 2017-11-06): ")
            close_date=input("종료일 (예: 2018-09-05): ")
            learning_course_info.append({'course_code':course_code,'course_name':course_name,'teacher':teacher,'open_date':open_date,'close_date':close_date,})
            file_data['total_course_info']={'learning_course_info':learning_course_info}
            now_learn=input("현재 수강하는 과목이 더 있습니까? (예: y/n): ")
        elif now_learn=='n':
            break
        else:
            now_learn("'y' or 'n' 으로 입력해주세요: ")

def select_information():
    print("아래 메뉴를 선택하세요.\n1. 전체 학생정보 조회\n검색 조건 선택\n2. ID 검색\n3. 이름 검색\n4. 나이 검색\n5. 주소 검색\n6. 과거 수강 횟수 검색\n7. 현재 강의를 수강중인 학생\n8. 현재 수강 중인 강의명\n9. 현재 수강 강사\n10. 이전 메뉴\n")
    select_num=input("메뉴를 선택하세요: ")
    load_json()
    if select_num=='1':
        for num in range(len(get_information)):
            print("학생 ID: %s, 학생 이름: %s"%(get_information[num]['student_ID'],get_information[num]['student_name']))
    else:
        search=input("검색어를 입력하세요: ")
        if select_num=='2':
            key='student_ID'
            search_word(search, key)
            if len(get_word)==1:
                print("학생 ID: %s, 학생 이름: %s"%(get_information[num]['student_ID'],get_information[num]['student_name']))

# * 이름:  전민하
# * 나이:  29
# * 주소:  동구 신암동
# * 수강 정보
# + 과거 수강 횟수:  2
# + 현재 수강 과목
# 강의 코드:  IB2929
# 강의명:  할렐루야
# 강사:  이현구
# 개강일:  2018-01-01
# 종료일:  2019-01-01

while True:
    print("\t<< json기반 주소록 관리 프로그램 >>\n1. 학생 정보입력\n2. 학생 정보조회\n3. 학생 정보수정\n4. 학생 정보삭제\n5. 프로그램 종료\n")
    select_num=input("메뉴를 선택하세요: ")
    if select_num=='1':
        insert_information()
        print(json.dumps(file_data, ensure_ascii=False, indent="\t"))
    elif select_num=='2':
        select_information()


