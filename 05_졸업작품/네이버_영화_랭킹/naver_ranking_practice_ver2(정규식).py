import urllib.request
from bs4 import BeautifulSoup
import re

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup=BeautifulSoup(html, 'html.parser') # BeautifulSoup 생성자에서 html을 파싱하고, 그 결과를 BeautifulSoup 객체로 반환

tags=soup.find_all('td')                # td 태그에서 영화명, 순위, 변동폭을 추출

title=re.compile('title=.*["][>](.*)</a>')  # 정규식으로 영화명 추출
t=title.findall(str(tags))                  # 추출 결과를 리스트로 저장

range_ac=re.compile('range ac["][>]([\d]{1,2})</td') # 순위 추출
r=range_ac.findall(str(tags))


up_down=re.compile('img alt[=]["]([a-z]{2,4})["]')   # 변동폭 추출
u=up_down.findall(str(tags))


note_pad = open('Naver_Ranking_ver2.csv','w',encoding='utf8')
note_pad.write("순위|\t영화명\t|\t변동폭\n")
for num in range(0,len(t)):
    if u[num]=='na':
        u[num]=' '
        note_pad.write(" %s\t|\t%s\t|\t%s%s\n"%(num+1,t[num],u[num],r[num]))
    elif u[num]=='up':
        u[num]='+'
        note_pad.write(" %s\t|\t%s\t|\t%s%s\n"%(num+1,t[num],u[num],r[num]))
    elif u[num]=='down':
        u[num]='-'
        note_pad.write(" %s\t|\t%s\t|\t%s%s\n"%(num+1,t[num],u[num],r[num]))

print("end")