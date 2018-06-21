import json

information={}
information['window']=True
information['humidifier']=False
information['dehumidifier']=False

with open('장비상태.json','w',encoding='utf8') as file:
    retJson = json.dumps(information, indent=4, sort_keys=True, ensure_ascii=False)
    file.write(retJson+"\n")