# 5 5 <== 해당 케이스에 대한 처리
def getTotalPage(m,n):
    if m%n==0:
        page=m/n
    else:
        page=(m/n)+1
    print("게시물 총 건수: "+str(m)+", 한 페이지에 보여줄 게시물 수: "+str(n)+", 총 페이지 수: "+str(int(page)))

def count(start, txt_list):
    try:
        while True:
            i=start
            total=int(txt_list[i])
            contents=int(txt_list[i+1])
            getTotalPage(total, contents)
            start+=2
    except ValueError:
        start+=2
        count(start, txt_list)
    except:
        print("프로그램을 종료합니다.")


f=open('condition.txt','r',encoding='UTF-8')
read_txt=f.read()
txt_list=read_txt.split()
start=0
count(start, txt_list)
