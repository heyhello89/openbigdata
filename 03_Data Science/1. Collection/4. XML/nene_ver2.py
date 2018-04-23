try:
    for num in range(3):
        for num2 in range(3):
            with open('V2_Big_Data/Nene_Data%s/nene%s.csv'%(num+1,num2+1),'r',encoding='utf8') as csv:
                csv.read()
except FileNotFoundError:
    with open('nene.csv',encoding='utf8') as record:
        read=record.read()
    with open('V2_Big_Data/Nene_Data%s/nene%s.csv'%(num+1,num2+1),'r',encoding='utf8') as csv:
        csv.write(read)