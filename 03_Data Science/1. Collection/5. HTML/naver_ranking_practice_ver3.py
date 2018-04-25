import urllib.request
from bs4 import BeautifulSoup
import re

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup=BeautifulSoup(html, 'html.parser')

# tags_title=soup.find_all('div','tit3')
tags_ac=soup.find_all('td')
# print(tags_title)
# print(tags_ac)
# tags=soup.find_all('div','tit3')
# tags_find=soup.find_all('img')
# tags_list=[]
# print(tags)

# title=re.compile('title=["].*["][>](.*)</a>.*img alt=["]([a-z]{2,4})["].*range ac["][>]([0-9]{1,2})[<][/td]',re.DOTALL)
# t=title.findall(str(tags))
# print(t)
# range_ac=re.compile('range ac["][>][\d]{1,2}[<][/][t][d]')
# r=range_ac.findall(str(tags))
# print(r)
#
# up_down=re.compile('img alt[=]["][a-z]{2,4}["]')
# u=up_down.findall(str(tags))
# print(u)

# print("%s\t%s\t%s"%(len(t),len(r),len(u)))
#
# def div(main, list1, list2):
#     for num in range(len(main)):
#         if num%2==0:
#             list1.append(main[num])
#         else:
#             list2.append(main[num])
#     return list1, list2
#
# def main1(tags):
#     for strings in list(tags):
#         if strings=='\n':
#             continue
#         else:
#             tags_list.append(strings)
#     return tags_list
#
# def main2(tags):
#     for num in range(len(tags)):
#         if tags[num].attrs['alt']=='na':
#             tags[num].attrs['alt']=' '
#         elif tags[num].attrs['alt']=='up':
#             tags[num].attrs['alt']='+'
#         elif tags[num].attrs['alt']=='down':
#             tags[num].attrs['alt']='-'
#         att.append(tags[num].attrs['alt'])
#     att[0:8]=[]
#     return att
#
# main1(tags_find[0].strings)
# main2(tags)
# div(tags_list, title, range_ac)
# div(att, rank, up_down)

# print(tags_list)
# print(att)
# print(title)
# print(range_ac)
# print(att)

# rank_num=0
# for num in range(10):
#     rank_num+=1
#     rank[num]=rank_num
    # "{0:0>2}".format(rank[num])
# print(rank)
# print(up_down)
#
# record = open('Naver Ranking','w',encoding='utf8')
# record.write("순위|\t영화명\t|\t변동폭\n")
# for count in range(len(title)):
#     record.write(" %s\t|\t%s\t|\t%s%s\n"%(rank[count],title[count],up_down[count],range_ac[count]))
# record.close()