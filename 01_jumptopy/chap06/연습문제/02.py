def mul(limit_su,num1):
    su_list=[]
    for i in range(1,limit_su+1):
        if i%num1==0:
            su_list.append(i)
    return su_list

def result(num_list1,num_list2):
    result_sum=0
    num_list1.extend(num_list2)
    num_list1 = list(set(num_list1))
    for i in range(0, len(num_list1)):
        result_sum += num_list1[i]
    return result_sum

input_su = input("범위, 첫번째수, 두번째수를 입력사헤요.(종료:프로그램 종료) : ").split()
input_su[0]=int(input_su[0])
input_su[1]=int(input_su[1])
input_su[2]=int(input_su[2])

print("0부터 %d 이하의 범위를 선택하셧습니다. 이 중에서"%input_su[0])
re_su=mul(input_su[0],input_su[1])
print("%d의 배수는 "%input_su[1],end='')
for i in range(0,len(re_su)):
    print("%d "%re_su[i],end='')
print("입니다.")
re_su2=mul(input_su[0],input_su[2])
print("%d의 배수는 "%input_su[2],end='')
for i in range(0,len(re_su2)):
    print("%d "%re_su2[i],end='')
print("입니다.")
sum=result(re_su,re_su2)
print("따라서 0부터 %d 이하의 범위내에서 %d과 %d의 배수의 총합은 %d입니다."%(input_su[0],input_su[1],input_su[2],sum))