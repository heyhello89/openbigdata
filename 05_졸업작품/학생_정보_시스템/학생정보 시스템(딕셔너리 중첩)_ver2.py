import json

def fmore_learning_course() :
    course_code=input("강의코드 (예: IB171106, OB0104 ..): ")
    course_name=input("강의명 (예: IOT 빅데이터 실무반): ")
    teacher=input("강사 (예: 이현구): ")
    open_date=input("개강일 (예: 2017-11-06): ")
    close_date=input("종료일 (예: 2018-09-05): ")
    learning_course_list.append(fdic_for_learning_course(close_date,open_date,course_code,course_name,teacher))
    
def fdic_for_learning_course(close_date,open_date,course_code,course_name,teacher):
    dic={}
    dic["close_date"]=close_date
    dic["open_date"]=open_date
    dic["course_code"]=course_code
    dic["course_name"]=course_name
    dic["teacher"]=teacher
    return dic

def fdic_for_total_course(list_learnig,num_of_learned_course):
    dic={}
    dic["learning_course_info"]=list_learnig
    dic["num_of_course_learned"]=num_of_learned_course
    return dic

def fdic_for_per_std(std_addr,std_id,std_age,std_name,total_course_dic):
    dic={}
    dic["address"] =std_addr
    dic["student_ID"] =std_id
    dic["student_age"] =std_age
    dic["student_name"] =std_name
    dic["total_course_info"] = total_course_dic
    return dic
def fput_std_dic():
    total_course_dic=fdic_for_total_course(learning_course_list,num_of_course_learned)
    std_dic=fdic_for_per_std(std_addr,std_id,std_age,std_name,total_course_dic)
    course_system_list.append(std_dic)
    print(course_system_list)
    
    
###############search
def fread_std(i):
    global course_system_list
    print("*학생 ID: "+course_system_list[i].get('student_ID'))
    print("*학생 이름: "+course_system_list[i].get('student_name'))
    print("*나이: "+str(course_system_list[i].get('student_age')))
    print("*주소: "+course_system_list[i].get('address'))
    print("*수강정보: ")
    print(" +과거 수강 횟수: "+str(course_system_list[i].get('total_course_info').get('num_of_course_learned')))
    if len(course_system_list[i].get('total_course_info').get('learning_course_info'))==0:
        print(" +현재 수강 과목: 0 ")
    else :
        for j in range(len(course_system_list[i].get('total_course_info').get('learning_course_info'))):
            print("   강의코드: "+str(course_system_list[i].get('total_course_info').get('learning_course_info')[j].get('course_code')))
            print("   강의 명: "+course_system_list[i].get('total_course_info').get('learning_course_info')[j].get('course_name'))
            print("   강사: "+course_system_list[i].get('total_course_info').get('learning_course_info')[j].get('teacher'))
            print("   개강일: "+course_system_list[i].get('total_course_info').get('learning_course_info')[j].get('open_date'))
            print("   종료일: "+course_system_list[i].get('total_course_info').get('learning_course_info')[j].get('close_date'))
            
def fread_std_sumary(index) :
    print("복수의 결과가 검색되었습니다.\n  ----- 요약 결과 -----  ")
    for i in index :
        print(">>  학생 ID: "+course_system_list[i].get('student_ID') +", 학생 이름:  "+course_system_list[i].get('student_name'))
        
def fsearch(parameter) :
    global index
    search=input(str_search)
    for i in range (len(course_system_list)):
        if course_system_list[i].get(parameter).find(search) >=0:
            index.append(i)
            print(index)
    if len(index) ==1 :
        fread_std(index[0])
    if len(index) >=2 :
        fread_std_sumary(index)
    index=[]
    
def fsearch_on_course(parameter1,parameter2):
    global index
    search=input(str_search)
    for i in range(len(course_system_list)):
        for j in range(len(course_system_list[i].get('total_course_info').get(parameter1))):
            if course_system_list[i].get('total_course_info').get(parameter1)[j].get(parameter2).find(search) >=0 :
                index.append(i)
    for i in index :
        fread_std(i)
    print()
    index=[]
    
    
####update
def fupdate_std(parameter):
    global index_from_id
    print("현재값: "+course_system_list[index_from_id].get(parameter))
    change=input("바꾸실 값을 입력하세요: ")
    course_system_list[index_from_id][parameter]=change
    
def fupdate_course(parameter):
    global index_from_id
    if parameter =="num_of_course_learned":
        print("현재값: "+course_system_list[index_from_id].get('total_course_info').get(parameter))
        change=input("바꾸실 값을 입력하세요: ")
        course_system_list[index_from_id].get('total_course_info')[parameter]=change
    elif parameter !="num_of_course_learned":
        print("현재값 :",end='')
        for j in range(len(course_system_list[index_from_id].get('total_course_info').get('learning_course_info'))) :
            print(course_system_list[index_from_id].get('total_course_info').get('learning_course_info')[j].get(parameter),end='')
        print()
        if len(course_system_list[index_from_id].get('total_course_info').get('learning_course_info')) == 1 :
            change=input("바꾸실 값을 입력하세요: ")
            course_system_list[index_from_id].get('total_course_info').get('learnig_course_info')[0][parameter]=change
        elif len(course_system_list[index_from_id].get('total_course_info').get('learning_course_info')) >1 :
            change_num = int(input("몇 번째 값을 바꾸시겠습니까? (예: 2) : "))
            change_num=-1
            change=input("바꾸실 값을 입력하세요: ")
            course_system_list[index_from_id].get('total_course_info').get('learnig_course_info')[change_num][parameter]=change

            
path='.'
file='\\ITT_Student.json'
while True :
    try :
        with open(path+file,'r',encoding='utf8') as ITT :
            ITT_data=json.load(ITT)
            course_system_list=ITT_data
        break
    except :
        print("파일을 찾을 수 없습니다. 아래 메뉴를 선택하세요")
        sel_fileerr_num=int(input("1.현재 경로에 새 파일 생성 \n2.경로 변경해서 다시 찾기 "))
        if sel_fileerr_num==1:
            f=open(path+file,'w')
            f.close()
            course_system_list=[]
            break
        elif sel_fileerr_num ==2 :
            path = input("변경된 경로를 입력하세요 (예 : c:\\user\\USER25\\Desktop) :")

str_start_menu ="""1. 학생 정보입력\n2. 학생 정보조회\n3. 학생 정보수정\n4. 학생 정보삭제\n5. 프로그램 종료\n메뉴를 선택하세요: """
str_read_menu ="""아래 메뉴를 선택하세요\n1. 전체 학생정보 조회\n--- 검색 조건 선택 ---\n2. ID검색\n3. 이름 검색\n4. 나이 검색\n5. 주소 검색\n6. 과거 수강 횟수 검색\n7. 현재 강의를 수강중인 학생\n8. 현재 수강중인 강의명\n9. 현재 수강 강사\n10. 이전 메뉴\n메뉴를 선택하세요: """
str_update_menu="1. 학생 이름\n2. 나이\n3. 주소\n4. 과거 수강 횟수\n5. 현재 수강 중인 강의 정보\n0. 이전 메뉴\n메뉴 번호를 입력하세요: "
str_update_munu_5="1. 강의 코드\n2. 강의명\n3. 강사\n4. 개강일\n5. 종료일\n0. 취소\n메뉴 번호를 입력하세요: "
str_delete_menu="삭제 유형을 선택하세요.\n1. 전체 삭제\n2. 현재 수강 중인 특정 과목정보 삭제\n3. 이전 메뉴\n메뉴 번호를 선택하세요: "
str_search="검색어를 입력하세요 :"

std_dic={}
total_course_dic={}
learning_course_list=[]
id_count=len(course_system_list)
index=[]
count=0
while True:
    print(''*20+'<<JSON기반 학생 정보 관리 프로그램 >>')
    sel_start_menu_num=int(input(str_start_menu))
    if sel_start_menu_num==5: #프로그램 종료
        break
    elif sel_start_menu_num==1:  #학생 정보 입력
        id_count+=1
        std_id='ITT{0:0>3}'.format(id_count)
        std_name=input("이름 (예: 홍길동):")
        std_age=input("나이 (예: 29):")
        std_addr=input("주소 (예: 대구광역시 동구 아양로 135): ")
        num_of_course_learned=int(input("과거 수강 횟수 (예: 1): "))
        learning_course_yN=input("현재 수강 과목이 있습니까? (예: y/n): ")
        if learning_course_yN=='y' :
            fmore_learning_course()
        elif learning_course_yN=='n' :
            learning_course_list.append({})
        while True:
            anoter_leaning_course=input("현재 수강하는 과목이 더 있습니까? (y/n): ")
            if anoter_leaning_course=='y':
                fmore_learning_course()
            elif anoter_leaning_course=='n':
                break
        fput_std_dic()
        continue
    elif sel_start_menu_num==2: #학생 정보 조회
        sel_read_menu_num=int(input(str_read_menu))
        if sel_read_menu_num==10 :
            print()
            continue
        elif sel_read_menu_num==1 : #전체 학생정보 조회
            for i in range(len(course_system_list)):
                fread_std(i)
        elif sel_read_menu_num==2 : #id검색
            fsearch("student_ID")
        elif sel_read_menu_num==3 : #이름검색
            fsearch("student_name")
        elif sel_read_menu_num==4 : #나이검색
            fsearch("student_age")
        elif sel_read_menu_num==5 : #주소검색
            fsearch("address")
        elif sel_read_menu_num==6 : #과거 수강횟수검색
            fsearch("num_of_course_learned")
        elif sel_read_menu_num==7 : #현재 강의 수강중인 학생 검색
            for i in range(len(course_system_list)):
                if len(course_system_list[i].get('total_course_info').get('learning_course_info'))!=0:
                    index.append(i)
                print(index)
            print("현재 강의를 수강 중인 학생: " ,end='')
            for idx in index:
                print('['+course_system_list[idx].get('student_name')+']',end='')
            index=[]
            print()
        elif sel_read_menu_num==8 : #현재 운영중인 강의명
            fsearch_on_course("learning_course_info",'course_name')
        elif sel_read_menu_num==9 : #현재 수업진행중인 강사
            fsearch_on_course("learning_course_info",'teacher')
    elif sel_start_menu_num==3: # 학생 정보 변경
        update_std_id_input=input('수정할 학생 ID를 입력하세요: ')
        sel_update_menu_num=int(input(str_update_menu))

        for i in range(len(course_system_list)):
            if course_system_list[i].get('student_ID')==update_std_id_input :
                index_from_id=i

        if sel_update_menu_num==0:  # 이전 메뉴
            print()
            continue
        elif sel_update_menu_num==1: #이름
            fupdate_std('student_name')
        elif sel_update_menu_num==2: #나이
            fupdate_std('student_age')
        elif sel_update_menu_num==3: #주소
            fupdate_std('address')
        elif sel_update_menu_num==4: #과거 수강횟수
            fupdate_course('num_of_course_learned')
        elif sel_update_menu_num==5: #현재 수강 과목
            sel_update_menu_5_num =int(input(str_update_munu_5))
            if sel_update_menu_5_num == 0: continue  #취소
            elif sel_update_menu_5_num==1:
                fupdate_course('course_code')
            elif sel_update_menu_5_num==2:
                fupdate_course('course_name')
            elif sel_update_menu_5_num==3:
                fupdate_course('teacher')
            elif sel_update_menu_5_num==4:
                fupdate_course('open_date')
            elif sel_update_menu_5_num==5:
                fupdate_course('close_date')


    elif sel_start_menu_num==4: #학생 정보 삭제
        del_std_id_input=input("삭제할 학생ID를 입력하세요: ")
        sel_delete_menu_num=int(input(str_delete_menu))

        for i in range(len(course_system_list)):
            if course_system_list[i].get('student_ID')==del_std_id_input :
                index_from_id=i

        if sel_delete_menu_num==1:
            del course_system_list[index_from_id]
        if sel_delete_menu_num==2:
            print("아이디 "+del_std_id_input+", 이름 "+course_system_list[index_from_id].get('student_name')+" 학생의 현재 수강 중인 과목 정보 삭제")
            for j in range(len(course_system_list[index_from_id].get('total_course_info').get('learning_course_info'))) :
                print(course_system_list[index_from_id].get('total_course_info').get('learning_course_info')[j].get('course_name'))
            if len(course_system_list[index_from_id].get('total_course_info').get('learning_course_info')) ==1:
                print('#### '+course_system_list[index_from_id].get('total_course_info').get('learning_course_info')[0].get('course_name')+' 수업이 삭제되었습니다 ####')
                del course_system_list[index_from_id].get('total_course_info').get('learning_course_info')[0]
                print()
            elif course_system_list[index_from_id].get('total_course_info').get('learning_course_info') > 1 :
                del_subject_num_input=int(input('몇 번째 과목을 삭제 하시겠습니까?'))
                del_subject_num_input-=1
                print('#### '+course_system_list[index_from_id].get('total_course_info').get('learning_course_info')[del_subject_num_input].get('course_name')+' 수업이 삭제되었습니다 ####')
                del course_system_list[index_from_id].get('total_course_info').get('learning_course_info')[del_subject_num_input]

        if sel_delete_menu_num==3:
            print()
            continue
        pass
with open(path+file,'w',encoding='utf8') as outfile :
    retJson= json.dumps(course_system_list,indent=4,sort_keys=True,ensure_ascii=False)
    outfile.write(retJson)
