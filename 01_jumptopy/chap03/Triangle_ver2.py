#coding: cp949

a=int(input("Ȧ���� �Է��ϼ���.: "))
b=int(a/2+1)
i=1
j=1
if a%2==0: 
    print("Ȧ���� �Է��ϼ���.")
    
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


