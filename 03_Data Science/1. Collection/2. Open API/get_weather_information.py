import urllib.request
import datetime
import json
import threading
import time


window_state = True
now_date=datetime.datetime.now()
get_date=now_date-datetime.timedelta(minutes=30)
ai_Mode=False

def get_request_url(url):
    req=urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    return response.read().decode('utf-8')


def getWeatherResult():
    base="http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData?"
    base_date=datetime.datetime.strftime(get_date, '%Y%m%d')
    base_time=datetime.datetime.strftime(get_date, '%H%M')
    nx='89'
    ny='91'
    type='json'
    pageNo='1'
    numOfRows='100'
    serviceKey='VNH7QeBnhzad%2B45QS4DMbIvJp0s%2Fx2iY9vdKxLYJJJEHMFFHDLr8HZJHuPgfjWRTg22OklmBOuSWznNeJktguQ%3D%3D'

    parameters = "base_date=%s&base_time=%s&nx=%s&ny=%s&_type=%s&ServiceKey=%s&pageNo=%s&numOfRows=%s"%(base_date,base_time,nx,ny,type,serviceKey,pageNo,numOfRows)
    url=base+parameters
    print(url)
    retData=get_request_url(url)
    return json.loads(retData)

def info_save(title,jsonSearch):
    with open('%s.json'%title, 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonSearch, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson+"\n")
    print("%s.json SAVED"%title)

def read_data(title):
    with open('%s.json'%title, 'r', encoding='utf8') as getfile:
        get_data=json.load(getfile)
        return get_data

def change_RN1(get_data):
    data=get_data['response']['body']['items']['item']
    for data in data:
        if data['category']=='RN1':
            data['fcstValue']=1
    return get_data

def update_scheduler():
    while True:
        if ai_Mode == False:
            continue
        else:
            time.sleep(3600)
            info_save('기상정보(ai)', getWeatherResult())
            weather_state=read_data('기상정보(ai)')
            equipment_state=read_data('장비상태')
            equipment_state=simulation_equipment(equipment_state, 'window', weather_state)
            equipment_state=simulation_equipment(equipment_state, 'dehumidifier', weather_state)
            equipment_state=simulation_equipment(equipment_state, 'humidifier', weather_state)
            info_save('장비상태(ai)', equipment_state)

def simulation_equipment(equipment_state, equipment, get_data):
    data=get_data['response']['body']['items']['item']
    category_data=[]
    if equipment=='window':
        category='RN1'
        eqm_value=0
    elif equipment=='humidifier':
        category='REH'
        eqm_value=0
    elif equipment=='dehumidifier':
        category='REH'
        eqm_value=0

    for data in data:
        if data['category']==category:
            category_data.append(data)

    max_Time=category_data[0]['fcstTime']
    for max in category_data:
        if max_Time < max['fcstTime']:
            max_Time = max['fcstTime']

    if equipment=='window':
        for value in category_data:
            if value['fcstTime']==max_Time:
                if value['fcstValue']>0:
                    equipment_state[equipment]=False
                else:
                    equipment_state[equipment]=True
        if equipment_state[equipment]==True:
            print("창문이 열렸습니다.")
        elif equipment_state[equipment]==False:
            print("창문이 닫혔습니다.")

    if equipment=='humidifier':
        for value in category_data:
            if value['fcstTime']==max_Time:
                if value['fcstValue']<35:
                    equipment_state[equipment]=True
                else:
                    equipment_state[equipment]=False
        if equipment_state[equipment]==True:
            print("가습기가 켜졌습니다.")
        elif equipment_state[equipment]==False:
            print("가습기가 꺼졌습니다.")

    if equipment=='dehumidifier':
        for value in category_data:
            if value['fcstTime']==max_Time:
                if value['fcstValue']>65:
                    equipment_state[equipment]=True
                else:
                    equipment_state[equipment]=False
        if equipment_state[equipment]==True:
            print("제습기가 켜졌습니다.")
        elif equipment_state[equipment]==False:
            print("제습기가 꺼졌습니다.")
    return equipment_state



equipment_state=read_data('장비상태')
info_save('기상정보(test)', getWeatherResult())
now_weather_state=read_data('기상정보(test)')
ai = threading.Thread(target=update_scheduler)
ai.daemon = True
ai.start()
equipment='window'
state=False
while True:
    select_num=input("1. 장비상태 확인\n2. 장비제어\n3. 인공지능 모드\n4. 시뮬레이션 모드\n5. 검색\n0. 종료\n번호를 선택하세요. : ")
    if select_num=='1':
        print("창문(window) : %s\n가습기(humidifier) : %s\n제습기(dehumidifier) : %s"%(equipment_state['window'],equipment_state['humidifier'],equipment_state['dehumidifier']))
    elif select_num=='2':
        while True:
            equipment_num=input("제어할 장비를 선택하세요.\n1. 창문\n2. 가습기\3. 제습기\0. 이전 단계\n번호를 선택하세요. : ")
            if equipment_num=='1':
                equipment='window'
            elif equipment_num=='2':
                equipment='humidifier'
            elif equipment_num=='3':
                equipment='dehumidifier'
            elif equipment_num=='0':
                break
            on_off=input("상태를 선택하세요.\n1. On(open)\n2. Off(close)\n번호를 선택하세요. : ")
            if on_off=='1':
                state=True
            elif on_off=='2':
                state=False
            try: equipment_state[equipment]=state
            except: continue

    elif select_num=='3':
        ai_Mode = not ai_Mode
        if ai_Mode==True: print("작동합니다.")
        else: print("정지합니다.")

    elif select_num=='4':
        change_weather_state=change_RN1(now_weather_state)
        equipment_state=simulation_equipment(equipment_state, 'window', change_weather_state)
        equipment_state=simulation_equipment(equipment_state, 'dehumidifier', change_weather_state)
        equipment_state=simulation_equipment(equipment_state, 'humidifier', change_weather_state)

    elif select_num=='5':
        channel=input("1. 주변 맛집\n2. 추천 드라마, 영화, 음악...\n3. 기사(조회수 순)\n번호를 입력하세요. : ")
        # if channel=='1':

    elif select_num=='0':
        break
info_save('장비상태', equipment_state)