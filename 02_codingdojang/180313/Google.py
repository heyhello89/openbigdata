#coding: cp949

i=1
sum=0

while True:
    count=str(i).count('8')
    sum+=count
    i+=1
    if i==10000:
        break
print(sum)

