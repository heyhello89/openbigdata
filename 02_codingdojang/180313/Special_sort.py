#coding: cp949

list_a=[-3,4,-2,2,7,-1,-4]

pos_list=[]
neg_list=[]

for i in list_a:
    if i>=0:
        pos_list.append(i)
    else:
        neg_list.append(i)

total_list=neg_list+pos_list

print(total_list)

