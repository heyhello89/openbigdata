import urllib.request
from bs4 import BeautifulSoup
import re

for page in range(1,51):
    html = urllib.request.urlopen('https://nenechicken.com/17_new/sub_shop01.asp?page=%s&ex_select=1&ex_select2=&IndexSword=&GUBUN=A'%page)
    soup=BeautifulSoup(html, 'html.parser')

    name=soup.find_all('div',attrs={'class':'shopName'})
    # for name in name:
    #     print(name)

    address=soup.find_all('div',attrs={'class':'shopAdd'})
    # for address in address:
    #     print(address.string)

    phone=soup.find_all('span',attrs={'class':'tooltiptext'})
    # for phone in phone:
    #     print(phone.string)

    note_pad = open('Nene_store_information_ver2.csv','a',encoding='utf8')
    note_pad.write("\t< %s page >\n번호|\t\t지점명\t\t\t|\t\t\t  주소  \t\t\t|\t전화번호\n"%(page))
    for num in range(len(name)):
        note_pad.write(" %s\t|\t%s \t|\t%s\t|\t%s\n"%(num+1,name[num].string,address[num].string,phone[num].string))

print("end")