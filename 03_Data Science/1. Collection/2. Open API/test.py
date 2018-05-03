import urllib.request
from bs4 import BeautifulSoup
import re

html = urllib.request.urlopen('http://news.naver.com/main/ranking/popularDay.nhn')
soup=BeautifulSoup(html, 'html.parser')

tags=soup.find_all('dl')
# tags_h4=soup.find_all('h4')

for tag in tags:
    tag=tag
    print(tag)