import json

def search_word_1st(get_information, search, main_key):
    find_list=[]
    for num in range(0, len(get_information)):
        for find_key,find_value in get_information[num].items():
            if search in find_value:
                if main_key==find_key:
                    find_list.append([num, find_key, find_value])
    return find_list

def search_word_2nd(get_information, search, main_key, second_key):
    find_list=[]
    for num in range(0, len(get_information)):
        for find_key, find_value in get_information[num][main_key].items():
            if search==find_value:
                if second_key==find_key:
                    find_list.append([num, find_key, find_value])
                    print(find_value)
                    print(find_list)
    return find_list

def search_word_3th(get_information, search, main_key, second_key, third_key):
    find_list=[]
    for num in range(0, len(get_information)):
        for num in range(0, len(get_information[num][main_key][second_key])):
            for find_key, find_value in get_information[num][main_key][second_key][num].items():
                if search in find_value:
                    if third_key==find_key:
                        find_list.append([num, find_key, find_value])
    return find_list

def search_course_learned(get_information, search, main_key, second_key):
    find_list=[]
    find_list_2=[]
    for num in range(0,len(get_information)):
        if len(get_information[num][main_key][second_key])!=0:
            find_list.append([num, main_key, len(get_information[num][main_key][second_key])])
        elif len(get_information[num][main_key][second_key])==0:
            find_list.append([num, main_key, len(get_information[num][main_key][second_key])])
    if search=='y':
        print_result(get_information, find_list)
    elif search=='n':
        print_result(get_information, find_list_2)
    else:
        search=input("'y' or 'n' 으로 입력해주세요: ")
        search_course_learned(get_information, search, main_key, second_key)

def print_result(get_information, find_list):
    if len(find_list)==1:
        num=find_list[0][0]
        print("* ID: %s"%get_information[num]['student_ID'])
        print("* 이름: %s"%get_information[num]['student_name'])
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

def insert_information(get_information):
    file_data_list=[]
    global file_data
    while True:
        file_data={}
        count=len(get_information)

        file_data['student_ID'] = ("ITT{0:0>3}".format(count+1))
        file_data['student_name'] = input("이름 (예: 홍길동): ")
        file_data['student_age'] = input("나이 (예: 29): ")
        file_data['address'] = input("주소 (예: 대구광역시 동구 아양로 135): ")
        num_of_course_learned=input("과거 수강 횟수 ( 예: 1): ")
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
                now_learn=input("현재 수강하는 과목이 더 있습니까? (예: y/n): ")
            elif now_learn=='n':
                if len(learning_course_info)==0:
                    learning_course_info.append({})
                break
            else:
                now_learn=input("'y' or 'n' 으로 입력해주세요: ")
        file_data['total_course_info']={'learning_course_info':learning_course_info,'num_of_course_learned':num_of_course_learned}
        file_data_list.append(file_data)
        get_information=file_data_list
        print(file_data_list)
        insert_continue=input("학생 정보를 더 입력하시겠습니까? (y/n): ")
        if insert_continue=='n':
            break
    print(file_data_list)
    print(get_information)
    return get_information

def select_information(get_information):
    print("아래 메뉴를 선택하세요.\n1. 전체 학생정보 조회\n검색 조건 선택\n2. ID 검색\n3. 이름 검색\n4. 나이 검색\n5. 주소 검색\n6. 과거 수강 횟수 검색\n7. 현재 강의를 수강중인 학생\n8. 현재 수강 중인 강의명\n9. 현재 수강 강사\n10. 이전 메뉴\n")
    select_num=input("메뉴를 선택하세요: ")
    main_key=''
    second_key='learning_course_info'
    if select_num=='1':
        for num in range(len(get_information)):
            print("학생 ID: %s, 학생 이름: %s"%(get_information[num]['student_ID'],get_information[num]['student_name']))
            main()
    elif select_num=='10':
        main()
    elif select_num=='7':
        main_key='total_course_info'
        search=input("검색어를 입력하세요 (y/n 로 입력하세요.): ")
        search_course_learned(get_information, search, main_key, second_key)
        main()

    search=input("검색어를 입력하세요: ")
    third_key='teacher'
    if select_num=='2':
        main_key='student_ID'
    elif select_num=='3':
        main_key='student_name'
    elif select_num=='4':
        main_key='student_age'
    elif select_num=='5':
        main_key='address'
    print_result(get_information, search_word_1st(get_information, search, main_key))

    main_key='total_course_info'
    if select_num=='6':
        second_key='num_of_course_learned'
        print_result(get_information, search_word_2nd(get_information, search, main_key, second_key))

    elif select_num=='9':
        print_result(get_information, search_word_3th(get_information, search, main_key, second_key, third_key))

    elif select_num=='8':
        third_key='course_code'
        find_list=search_word_3th(get_information, search, main_key, second_key, third_key)
        if len(find_list)>0:
            print_result(get_information, find_list)
        else:
            third_key='course_name'
            find_list_2=search_word_3th(get_information, search, main_key, second_key, third_key)
            print_result(get_information, find_list_2)

def update_search(get_information, ):
    search=input("정보를 수정할 학생의 ID를 입력해주세요. : ")
    find_list=search_word_1st(get_information, search, 'student_ID')
    print_result(get_information, find_list)
    return find_list

def update_main_key(get_information, find_list, main_key):
    print("현재 값: %s"%get_information[find_list[0][0]][main_key])
    get_information[find_list[0][0]][main_key]=input("바꾸실 값을 입력하세요. :")

def update_2nd_key(get_information, find_list, second_key):
    print("현재 값: %s"%get_information[find_list[0][0]]['total_course_info'][second_key])
    get_information[find_list[0][0]]['total_course_info'][second_key]=input("바꾸실 값을 입력하세요. :")

def update_3th_key(get_information, find_list, third_key):
    if len(get_information[find_list[0][0]]['total_course_info']['learning_course_info'])==1:
        print("수강과목 현재 값: %s"%(get_information[find_list[0][0]]['total_course_info']['learning_course_info'][0][third_key]))
        get_information[find_list[0][0]]['total_course_info']['learning_course_info'][0][third_key]=input("바꾸실 값을 입력하세요. :")
    elif len(get_information[find_list[0][0]]['total_course_info']['learning_course_info'])>1:
        update_code=input("수정할 내용의 수강과목 코드를 입력해 주세요. :")
        for num in range(0,len(get_information[find_list[0][0]]['total_course_info']['learning_course_info'])):
            for find_key, find_value in get_information[find_list[0][0]]['total_course_info']['learning_course_info'][num].items():
                if find_key=='course_code':
                    if find_value==update_code:
                        print("%s) 수강과목 현재 값: %s"%(num,get_information[find_list[0][0]]['total_course_info']['learning_course_info'][num][third_key]))
                        get_information[num]['total_course_info']['learning_course_info'][num][third_key]=input("바꾸실 값을 입력하세요. :")

def update_information(get_information):
    find_list=update_search(get_information)
    while len(find_list)!=1:
        find_list=update_search(get_information)
    update_num=input("수정할 항목을 선택하세요.\n1. 학생 이름\n2. 나이\n3. 주소\n4. 과거 수강 횟수\n5. 현재 수강 중인 강의 정보\n0. 이전 메뉴\n메뉴 번호를 입력하세요: ")
    if update_num=='1':
        update_main_key(get_information, find_list, 'student_ID')
    elif update_num=='2':
        update_main_key(get_information, find_list, 'student_age')
    elif update_num=='3':
        update_main_key(get_information, find_list, 'address')
    elif update_num=='4':
        update_2nd_key(get_information, find_list, 'num_of_course_learned')
    elif update_num=='5':
        update_num_learned_info=input("1. 강의 코드\n2. 강의명\n3. 강사\n4. 개강일\n5. 종료일\n0. 취소\n메뉴 번호를 입력하세요: ")
        if update_num_learned_info=='1':
            update_3th_key(get_information, find_list, 'course_code')
        elif update_num_learned_info=='2':
            update_3th_key(get_information, find_list, 'course_name')
        elif update_num_learned_info=='3':
            update_3th_key(get_information, find_list, 'teacher')
        elif update_num_learned_info=='4':
            update_3th_key(get_information, find_list, 'open_date')
        elif update_num_learned_info=='5':
            update_3th_key(get_information, find_list, 'close_date')
        elif update_num_learned_info=='0':
            pass
    elif update_num=='0':
        main()

def delete_course(get_information, find_list):
    if len(get_information[find_list[0][0]]['total_course_info']['learning_course_info'])==1:
        del get_information[find_list[0][0]]['total_course_info']['learning_course_info'][0]
    elif len(get_information[find_list[0][0]]['total_course_info']['learning_course_info'])>1:
        update_code=input("삭제할 내용의 수강과목 코드를 입력해 주세요. :")
        for num in range(0,len(get_information[find_list[0][0]]['total_course_info']['learning_course_info'])):
            for find_key, find_value in get_information[find_list[0][0]]['total_course_info']['learning_course_info'][num].items():
                if find_key=='course_code':
                    if find_value==update_code:
                        del get_information[find_list[0][0]]['total_course_info']['learning_course_info'][num]

def delete_information(get_information):
    delete_num=input("삭제 유형을 선택하세요.\n1. 전체 삭제\n2. 현재 수강 중인 특정 과목정보 삭제\n3. 이전 메뉴\n메뉴 번호를 선택하세요: ")
    delete_std=input("삭제할 학생의 ID를 입력하세요: ")

    find_list=search_word_1st(get_information, delete_std, 'student_ID')
    print(find_list)

    if delete_num=='1':
        del get_information[find_list[0][0]]
    elif delete_num=='2':
        delete_course(get_information,find_list)
    elif delete_num=='3':
        main()

def make_json_file():
    make_order=str(input("파일을 찾을 수 없습니다.\n1. 파일을 새로 만들겠습니다.\n2. 경로를 입력하겠습니다.\n1, 2로 선택하세요. : "))
    while True:
        if make_order=='1':
            json_file_name=input("파일명을 입력해주세요. (ex.ITT_Student.json): ")
            break
        elif make_order=='2':
            json_file_name=input("경로를 입력해주세요. (ex.ITT_Student.json): ")
            break
        else:
            make_json_file()
    return json_file_name

def main():
    while True:
        print("\t<< json기반 주소록 관리 프로그램 >>\n1. 학생 정보입력\n2. 학생 정보조회\n3. 학생 정보수정\n4. 학생 정보삭제\n5. 프로그램 종료\n")
        select_num=input("메뉴를 선택하세요: ")
        if select_num=='1':
            insert_information(get_information)
            print(json.dumps(file_data, ensure_ascii=False, indent="\t"))
        elif select_num=='2':
            select_information(get_information)
        elif select_num=='3':
            update_information(get_information)
        elif select_num=='4':
            delete_information(get_information)
        elif select_num=='5':
            print("학생 정보 관리 프로그램을 종료합니다.")
            break
    with open(json_file_name,'w',encoding='UTF8') as file_make:
        file_data_list=json.dumps(file_data, ensure_ascii=False, sort_keys=True, indent=4)
        file_make.write(file_data_list)


try:
    global json_file_name
    json_file_name='ITT_Student.json'
    with open(json_file_name,'r',encoding='utf8') as selection:
        get_info=json.load(selection)
        get_information=get_info
except FileNotFoundError:
    json_file_name=make_json_file()
    get_name=str(json_file_name)
    get_information=[]
    get_information=insert_information(get_information)
main()
