import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame
html = """
<html>
         <tbody>
            <tr><td colspan="8" class="blank01"></td></tr>
            <!-- 예제
            <tr>
               <td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g50.gif" alt="50" width="14" height="13"></td>
               <td class="title"><a href="#">트랜스포머</a></td>
               <td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10"></td>
               <td class="range ac">7</td>
            </tr>
            -->
            
            <tr>
               
                  <td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r01.gif" alt="01" width="14" height="13"></td>
               
               <td class="title">
                  <div class="tit3">
                     <a href="/movie/bi/mi/basic.nhn?code=162249" title="램페이지">램페이지</a>
                  </div>
               </td>
               <!-- 평점순일 때 평점 추가하기  -->  
               
               <!----------------------------------------->  
               
               <td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_na_1.gif" alt="na" width="7" height="10" class="arrow"></td>
               <td class="range ac">0</td>
               
               
            </tr>
               
               
            
            <tr>
               
                  <td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r02.gif" alt="02" width="14" height="13"></td>
               
                  
               
               
               <td class="title">
                  <div class="tit3">
                     <a href="/movie/bi/mi/basic.nhn?code=136315" title="어벤져스: 인피니티 워">어벤져스: 인피니티 워</a>
                  </div>
               </td>
               <!-- 평점순일 때 평점 추가하기  -->  
               
               <!----------------------------------------->  
               
               <td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
               <td class="range ac">1</td>
               
               
            </tr>
               
               <tr><td colspan="8" class="blank01"></td></tr>
         </tbody>
</html>
"""

soup=BeautifulSoup(html, 'html.parser')
# print("<soup>")
# print(soup)

tags=soup.tbody
# print(tags)

sub_tag=tags.tr
# print(sub_tag)

tags=soup.find_all('tbody')
# print(tags)
print(tags[0])
# print(tags[0].strings)
# for tag in tags[0].strings:
#     print(tag)

# tags=soup.find_all('img')
# print(tags)

# attribute=tags[3].attrs['alt']
# print(attribute)