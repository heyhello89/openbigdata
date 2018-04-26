import json
from collections import OrderedDict
import re
find_list=[]

def load_json():
    global get_information
    with open('ITT_Student.json','r',encoding='utf8') as selection:
        get_information=json.load(selection)
    return get_information

def search_word_1st(search, main_key):
    for num in range(0, len(get_information)):
        for find_key,find_value in get_information[num].items():
            if str(search) in str(find_value):
                if main_key==find_key:
                    find_list.append([num, find_key, find_value])
    return find_list

def search_word_2nd(search, main_key, second_key):
    for num in range(0, len(get_information)):
        for find_key, find_value in get_information[num][main_key].items():
            if second_key==find_key:
                if int(search)==int(find_value):
                    find_list.append([num, find_key, find_value])
                    print(find_list)

    return find_list

def search_word_3th(search, main_key, second_key, third_key):
    for num in range(0, len(get_information)):
        for find_key, find_value in get_information[num][main_key][second_key].items():
            if search in find_value:
                if third_key==find_key:
                    find_list.append([num, find_key, find_value])
    return find_list

        # for find_key,find_value in get_information[num]['total_course_info']['learning_course_info'][0].items():
        #     if search in str(find_value):
        #         if key==find_key:
        #             find_list.append([num, find_key, find_value])
    print(find_list)
    return find_list


def print_result(find_list):
    get_information=load_json()
    if len(find_list)==1:
        num=find_list[0][0]
        print("* 이름: %s"%get_information[num]['student_ID'])
        print("* 나이: %s"%get_information[num]['student_age'])
        print("* 주소: %s"%get_information[num]['address'])
        print("* 수강 정보")
        print(" + 과거 수강 횟수: %s"%get_information[num]['total_course_info']['num_of_course_learned'])
        print(" + 현재 수강 과목: ")
        for count in range(len(get_information[num]['total_course_info']['learning_course_info'])):
            print("  %s)"%(count+1))
            print("  강의 코드: %s"%get_information[num]['total_course_info']['learning_course_info'][count]['course_code'])
            print("  강의명: %s"%get_information[num]['total_course_info']['learning_course_info'][count]['course_name'])
            print("  강사: %s"%get_information[num]['total_course_info']['learning_course_info'][count]['teacher'])
            print("  개강일: %s"%get_information[num]['total_course_info']['learning_course_info'][count]['open_date'])
            print("  종료일: %s"%get_information[num]['total_course_info']['learning_course_info'][count]['close_date'])
    elif len(find_list)==0:
        pass
    else:
        print("  ----- 요약 결과 -----  ")
        for num in range(0,len(find_list)):
            print("학생 ID: %s, 학생 이름: %s"%(get_information[num]['student_ID'],get_information[num]['student_name']))

def insert_information():
    global file_data
    file_data = OrderedDict()
    get_infomation=load_json()
    count=len(get_infomation)
    file_data['student_ID'] = ("ITT{0:0>3}".format(count+1))
    file_data['student_name'] = input("이름 (예: 홍길동): ")
    file_data['student_age'] = input("나이 (예: 29): ")
    file_data['address'] = input("주소 (예: 대구광역시 동구 아양로 135): ")
    file_data['total_course_info']['num_of_course_learned'] = input("과거 수강 횟수 ( 예: 1): ")
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
    get_information=load_json()
    print("아래 메뉴를 선택하세요.\n1. 전체 학생정보 조회\n검색 조건 선택\n2. ID 검색\n3. 이름 검색\n4. 나이 검색\n5. 주소 검색\n6. 과거 수강 횟수 검색\n7. 현재 강의를 수강중인 학생\n8. 현재 수강 중인 강의명\n9. 현재 수강 강사\n10. 이전 메뉴\n")
    select_num=input("메뉴를 선택하세요: ")
    load_json()
    if select_num=='1':
        for num in range(len(get_information)):
            print("학생 ID: %s, 학생 이름: %s"%(get_information[num]['student_ID'],get_information[num]['student_name']))
    elif select_num=='10':
        main()

    search=input("검색어를 입력하세요: ")
    main_key=''
    second_key='learning_course_info'
    third_key='teacher'
    if select_num=='2':
        main_key='student_ID'
    elif select_num=='3':
        main_key='student_name'
    elif select_num=='4':
        main_key='student_age'
    elif select_num=='5':
        main_key='address'
    print_result(search_word_1st(search, main_key))

    main_key='total_course_info'
    if select_num=='6':
        second_key='num_of_course_learned'
        # for num in range(0, len(get_information)):
        print_result(search_word_2nd(search, main_key, second_key))
    if select_num=='7':
        find_list=[]
        for num in range(0,len(get_information)):
            if len(get_information[num][main_key][second_key])==0:
                pass
            else:
                find_list.append([num, main_key, len(get_information[num][main_key[second_key]])])
                print(find_list)
    if select_num=='9':
        pass


    if select_num=='8':
        third_key='course_code'
        find_list=search_word_3th(search, main_key, second_key, third_key)
        third_key='course_name'
        find_list_2=search_word_3th(search, main_key, second_key, third_key)
        if len(find_list)<1:
            print_result(find_list)
        else:
            print_result(find_list_2)
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
def main():
    while True:
        print("\t<< json기반 주소록 관리 프로그램 >>\n1. 학생 정보입력\n2. 학생 정보조회\n3. 학생 정보수정\n4. 학생 정보삭제\n5. 프로그램 종료\n")
        select_num=input("메뉴를 선택하세요: ")
        if select_num=='1':
            insert_information()
            print(json.dumps(file_data, ensure_ascii=False, indent="\t"))
        elif select_num=='2':
            select_information()


main()