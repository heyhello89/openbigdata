import urllib.request
from bs4 import BeautifulSoup
import re
from pandas import DataFrame
rank=[num for num in range(51)]
name=[]
fluctuation=[]
fluctuation_num=[]

html = urllib.request.urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup=str(BeautifulSoup(html,'html.parser'))


p=re.compile('\<[a-zA-Z]+.*class\=\"range\sac\".*([0-9]+).*[\>][^<]*\<\/[a-zA-Z]+\>')
# print(p.findall(soup))
fluc_num=p.findall(soup)
del fluc_num[0]
#변동
p=re.compile('\<[a-zA-Z]+.*alt\=\"([a-z]+).*[\>][^<]*\<\/[a-zA-Z]+\>')
# print(p.findall(soup))
fluc=p.findall(soup)
del fluc[0]
#영화이름
# p=re.compile('\<a\shref[^\>]*title\=[\"\']?([^\>\'\"]*)[\"\']?\>')
p=re.compile('\<a\shref\=[\'\"]?[^\>\'\"\#]*[\"\']?\stitle\=[\"\']?([^\>\'\"]*)[\"\']?\>')
# print(p.findall(soup))
name=p.findall(soup)
#영화 순위
p=re.compile('\<[a-zA-Z]+.*alt\=\"([0-9]+).*[\>][^<]*\<\/[a-zA-Z]+\>')
# print(p.findall(soup))
rank=p.findall(soup)
del rank[0]
result=[]
fluc_total=[]
for i in range (50):
    fluc_total.append(fluc[i]+fluc_num[i])
    result.append([rank[i]]+[name[i]]+[fluc_total[i]])
rank_table= DataFrame(result,columns=('순위','영화명','등락'))
print(rank_table)


rank_table.to_csv('naver_movie_rank1',encoding='utf8',mode='w',index=False)