#coding: cp949
age=int(input("���̸� �Է��ϼ���. : "))
addmission=0
rank="����"

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
            break
        else:
            print("���ϴ�",rank,"����̸�, ����� ",addmission,"�� �Դϴ�.")
            pay_type=int(input("��� ������ �����ϼ���. (1:����, 2:���� ���� �ſ� ī��): "))

            if pay_type==1:
                pay=int(input("����� �Է��ϼ���. :"))
                if pay<addmission:
                    print(addmission-pay,"�� ���ڶ��ϴ�. �Է��Ͻ�",pay,"���� ��ȯ�մϴ�.")
                elif pay==addmission:
                    print("�����մϴ�. Ƽ���� �����մϴ�.")
                else:
                    print("�����մϴ�. Ƽ���� �����ϰ� �Ž�����",pay-addmission,"���� ��ȯ�մϴ�.")
            elif pay_type==2:
                print("(���� �ݾ��� 10% ����, 60~65�� ����� �߰� 5% ����)")
                if 60<=age<=65:
                    print(int(addmission*0.9*0.95),"�� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�.")
                else:
                    print(addmission*0.9,"�� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�.")
            break





