import urllib.request
from bs4 import BeautifulSoup
import re

for page in range(1,51):
    html = urllib.request.urlopen('https://nenechicken.com/17_new/sub_shop01.asp?page=%s&ex_select=1&ex_select2=&IndexSword=&GUBUN=A'%page)
    soup=BeautifulSoup(html, 'html.parser')

    tags=soup.find_all('td')
    # print(tags)

    name=re.compile('shopName["][>](.*)</div>')
    name_list=name.findall(str(tags))
    # print(name_list)
    # print(len(name_list))

    address=re.compile('codeAddress[(][\'](.*)[\'][)][;]["]')
    address_list=address.findall(str(tags))
    # print(address_list)
    # print(len(address_list))

    phone=re.compile('tooltiptext["][>](.*)</span>')
    phone_list=phone.findall(str(tags))
    # print(phone_list)
    # print(len(phone_list))

    note_pad = open('Nene_store_information.csv','a',encoding='utf8')
    note_pad.write("\t< %s page >\n번호|\t\t지점명\t\t\t|\t\t\t  주소  \t\t\t|\t전화번호\n"%(page))
    for num in range(len(name_list)):
        note_pad.write(" %s\t|\t%s \t|\t%s\t|\t%s\n"%(num+1,name_list[num],address_list[num],phone_list[num]))

print("end")