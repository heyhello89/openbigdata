#coding: cp949

name="������,���翵,����ǥ,���翵,�ڹ�ȣ,������,���翵,������,�ֽ���,�̼���,�ڿ���,�ڹ�ȣ,������,����ȯ,���缺,������,������"
list_name=[]
i=0
while True:
    list_name.append(name[i:i+3])
    i+=4
    if i>len(name):
        break
set_name=set(list_name)
asc_name=list(set_name)
asc_name.sort()
print(name)
print("\n�达 :",name.count('��'),"ȸ")
print("�̾� :",name.count('��'),"ȸ")
print("\"���翵\" :",name.count('���翵'),"ȸ")
print("�ߺ� ���� :",set_name)
print("��������:",asc_name)
