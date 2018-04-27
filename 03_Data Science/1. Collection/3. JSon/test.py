import json
from collections import OrderedDict
import re

def load_json():
    global get_information
    with open('ITT_Student.json','r',encoding='utf8') as selection:
        get_information=json.load(selection)
    return get_information

def load_json_2():
    with open('ITT_Student.json',encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        json_big_data = json.loads(json_string)
    return  json_big_data

key_list=list(load_json())
# key_list_2=list(load_json_2()[0])
print(key_list)
# print(key_list_2)
# def search_main(search, key):
#     find_list=[]
#     for num in range(0, len(load_json())):
#         for find_key,find_value in load_json()[num].items():
#             if search in str(find_value):
#                 if key==find_key:
#                     find_list.append([num, find_key, find_value])
#
# search_test=re.compile('[\'](.*)[\':][ ].*'+input()+'.*[ ]',re.MULTILINE)
# find=search_test.findall(str(load_json()).strip(),)
# print(find)