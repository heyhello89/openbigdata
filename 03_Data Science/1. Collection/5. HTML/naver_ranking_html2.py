import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup=BeautifulSoup(html, 'html.parser')
# print("<soup>")
# print(soup)
# print(soup.prettify())

tags=soup.tbody
# print(tags)

sub_tag=tags.tr
# print(sub_tag)

tags=soup.find_all('td')
# print(tags)
for num in tags:
    print(num)
# print(tags[0].strings)
# for tag in tags[0].strings:
#     print(tag)
# list=list(tags[0].strings)
# for a in list:
#     list.remove('\n')
# print(list)




tags=soup.find_all('img')
# print(tags)

# att=[]
# for attribute in tags.attrs['alt']:
#     att.append(attribute)
# print(att)
# for num in range(len(tags)):
#     att.append(tags[num].attrs['alt'])
# print(att)