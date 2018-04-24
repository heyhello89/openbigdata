# py -m pip install beautifulsoup4
from bs4 import BeautifulSoup
html='''
<td class="title">
<div class="tit3">
<a href="/movie/bi/mi/basic.nhn?code=158191"title="1987">1987
</a></div>/td>
'''
# <a title <= 마우스 타겟시 설명 메세지 출력
soup=BeautifulSoup(html,'html.parser')

# print(soup)

# tag=soup.td
# print(tag)

# tag=soup.div
# print(tag)

tag=soup.a
# print(tag)

print(tag.name)
print(tag.attrs)
print(tag.string) # 태그 안의 값(태그가 끝나기 전)
print(tag.text)   # tag.string과 같다. 차이점이 존재하긴 하지만 뒤에서 볼 것이다.