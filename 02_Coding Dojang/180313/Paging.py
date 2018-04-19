#coding: cp949

m=int(input("총건수 : "))
n=int(input("페이지당 게시물 수 : "))

result=int(m/n)
if m%n>0:
    result=result+1
print("총 페이지 수 :",result)
