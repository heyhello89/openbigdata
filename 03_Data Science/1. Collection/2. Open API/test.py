import urllib.request
from bs4 import BeautifulSoup
import re

html = urllib.request.Request('http://www.melon.com/chart/index.htm')
main = urllib.request.urlopen(html)
soup=BeautifulSoup(main, 'html.parser')

tags=soup.find_all('div',attrs={'class':'rank_music'})
# tags_h4=soup.find_all('h4')

# for tag in tags:
    # tag=tag
print(tags)