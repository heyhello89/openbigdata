import urllib
from bs4 import BeautifulSoup as BS
from pandas import DataFrame
import csv
max_page=50
result=[]
index='index'
count=1

for page_idx in range(1,max_page+1):
    nene_url='https://nenechicken.com/17_new/sub_shop01.asp?page=%s&ex_select=1&ex_select2=&IndexSword=&GUBUN=A'%(str(page_idx))
    print(nene_url)
    response=urllib.request.urlopen(nene_url)
    soupData=BS(response.read().decode('UTF-8'),'html.parser')

    store_name=soupData.find_all('div',{'class':'shopName'})
    store_addr=soupData.find_all('div',{'class':'shopAdd'})
    store_phone=soupData.find_all('span',{'class':'tooltiptext'})
    for i in range(len(store_addr)):
        result.append([str(count)]+[store_name[i].text]+[store_addr[i].text]+[store_phone[i].text])
        count+=1
print(result)

nene_table=DataFrame(result,columns=('번호','지점명','주소','전화번호'))
nene_table.to_csv('.\\nene_지점_to_page50.csv',encoding='utf8',mode='w',index=False)