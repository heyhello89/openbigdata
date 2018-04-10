import math

i_se=0
def getTotalPage(m,n):
    result = math.ceil(int(m)/int(n))
    return result

try:
    f=open('condition.txt','r',encoding='UTF-8')
    select_con=f.read().split()
    for i in range(0,math.ceil(len(select_con)/2)):
        total_page=getTotalPage(select_con[i_se],select_con[i_se+1])
        print("게시물 총 건수 : %s, 한 페이지에 보여줄 게시물 수 : %s , 총 페이지수 : %d"%(select_con[i_se],select_con[i_se+1],total_page))
        i_se += 2

except:
    try:
        i_se+=2
        for i in range(i+1,math.ceil(len(select_con)/2)):
            total_page=getTotalPage(select_con[i_se],select_con[i_se+1])
            print("게시물 총 건수 : %s, 한 페이지에 보여줄 게시물 수 : %s , 총 페이지수 : %d"%(select_con[i_se],select_con[i_se+1],total_page))
            i_se += 2
    except:
        pass