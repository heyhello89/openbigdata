#http://nenechicken.com/subpage/where/where_list.asp?target_step1=%EC%A0%84%EC%B2%B4&target_step2=%EC%A0%84%EC%B2%B4&proc_type=step1
import urllib.request
import os
from pandas import DataFrame
import xml.etree.ElementTree as ET
import datetime

result = []
dir_name = "V4_BigData"
dir_delimiter = "\\"
nene_dir = "Nene_Data"
nene_file = "nene"
csv = ".csv"
record_limit = 3
now_date=datetime.datetime.now()
date = datetime.datetime.strftime(now_date, '%Y-%m-%d_%H%M%S')

def make_dir(dir_index) :
    os.mkdir(dir_name + dir_delimiter + nene_dir+str(dir_index))
    return None

def make_nene(dir_index) :
    destination_csv = dir_name + dir_delimiter + nene_dir + str(dir_index) + dir_delimiter + str(date) + csv
    nene_table.to_csv(destination_csv,encoding="utf8", mode='w', index=True)
    return None

def dir_index():
    dir_num=len(os.listdir(dir_name))
    if len(os.listdir(dir_name + dir_delimiter + nene_dir+str(dir_num)))==3:
        dir_num+=1
        make_dir(dir_num)
    return dir_num


response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))
xml = response.read().decode('UTF-8')
root = ET.fromstring(xml)

for element in root.findall('item'):
    store_name = element.findtext('aname1')
    store_sido = element.findtext('aname2')
    store_gungu = element.findtext('aname3')
    store_address = element.findtext('aname5')
    result.append([store_name]+[store_sido]+[store_gungu]+[store_address])

nene_table = DataFrame(result,columns=('sotre','sido','gungu','store_address'))

if not os.path.exists(dir_name):
    os.mkdir(dir_name)
if not os.path.exists(dir_name + dir_delimiter + nene_dir + '1'):
    make_dir(1)

make_nene(dir_index())

print("End")