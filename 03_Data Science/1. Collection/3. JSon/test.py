import json
from collections import OrderedDict
import re

def load_json():
    global get_information
    with open('ITT_Student.json','r',encoding='utf8') as selection:
        get_information=json.load(selection)
    return get_information

list=list(load_json()[1].keys())
print(list)

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