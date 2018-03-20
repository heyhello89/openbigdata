#coding: cp949

a=int(input("홀수를 입력하세요.: "))
b=int(a/2+1)
i=1
j=1
if a%2==0: 
    print("홀수를 입력하세요.")
    
else:
    while True:
        print(" "*(b-j)+"*"*i)
        j+=1
        i+=2
        if i==a:
            while True:
                print(" "*(b-j)+"*"*i)
                j-=1
                i-=2
                if i<0:
                    break
            break


