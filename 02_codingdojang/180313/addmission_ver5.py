#coding: cp949

addmission=0
rank="����"
ticket_free=3
ticket_discount=5
ticket_count=0

while ticket_free!=0:
    ticket_count+=1
    age=int(input("���̸� �Է��ϼ���. : "))

    while True:
        if age<0:
            age=int(input("���̸� �ٽ� �Է��ϼ���. :"))
        else:
            if age<4 :
                addmission=0
                rank="����"
            elif age<14 :
                addmission=2000
                rank="���"
            elif age<19 :
                addmission=3000
                rank="û�ҳ�"
            elif age<66 :
                addmission=5000
                rank="����"
            else:
                addmission=0
        
            if addmission==0:
                print("���ϴ�",rank,"����̸�, ����� ���� �Դϴ�.")
                ticket_count-=1
                break
            else:
                print("���ϴ�",rank,"����̸�, ����� ",addmission,"�� �Դϴ�.")
                pay_type=int(input("��� ������ �����ϼ���. (1:����, 2:���� ���� �ſ� ī��): "))

                if pay_type==1:
                    pay=int(input("����� �Է��ϼ���. :"))
                    if pay<addmission:
                        print(addmission-pay,"�� ���ڶ��ϴ�. �Է��Ͻ�",pay,"���� ��ȯ�մϴ�.")
                        ticket_count-=1                       
                    elif pay==addmission:
                        print("�����մϴ�. Ƽ���� �����մϴ�.")
                    else:
                        print("�����մϴ�. Ƽ���� �����ϰ� �Ž�����",pay-addmission,"���� ��ȯ�մϴ�.")
                elif pay_type==2:
                    print("(���� �ݾ��� 10% ����, 60~65�� ����� �߰� 5% ����)")
                    if 60<=age<=65:
                        print(int(addmission*0.9*0.95),"�� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�.")
                    else:
                        print(int(addmission*0.9),"�� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�.")
                break
               
    if ticket_count==0:
        continue
    elif ticket_count%7==0:
        ticket_free-=1
        print("�����մϴ�. 1�ֳ� �̺�Ʈ�� ��÷�Ǿ����ϴ�. ���� ���� Ƽ���� �����մϴ�. �ܿ� ����Ƽ��:",ticket_free,"��")
    elif ticket_count%4==0:
        ticket_discount-=1
        print("�����մϴ�. ����ȸ���� ���� �̺�Ʈ�� ��÷�Ǿ����ϴ�. ���� ȸ�� ���� Ƽ���� �����մϴ�. �ܿ� ����Ƽ��:",ticket_discount,"��")
    else:
        continue
        
