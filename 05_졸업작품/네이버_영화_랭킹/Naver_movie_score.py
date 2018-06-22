import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup=BeautifulSoup(html, 'html.parser') # BeautifulSoup 생성자에서 html을 파싱하고, 그 결과를 BeautifulSoup 객체로 반환
url=soup.find_all('a')                # a 태그에서 url 추출

for tag in url[35:85]:
