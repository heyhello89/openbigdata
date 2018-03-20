#coding: cp949

name="이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"
list_name=[]
i=0
while True:
    list_name.append(name[i:i+3])
    i+=4
    if i>len(name):
        break
set_name=set(list_name)
asc_name=list(set_name)
asc_name.sort()
print(name)
print("\n김씨 :",name.count('김'),"회")
print("이씨 :",name.count('이'),"회")
print("\"이재영\" :",name.count('이재영'),"회")
print("중복 제거 :",set_name)
print("오름차순:",asc_name)
