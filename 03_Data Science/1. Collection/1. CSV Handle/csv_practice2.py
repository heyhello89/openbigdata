import csv, math

def get_cvs_colInstance(access_key):
    col_instance=[]
    col_index=data[0].index(access_key)
    for row in data[1:]:
        col_instance.append(row[col_index])

    return col_instance

def get_cvs_rowInstance(access_key):
    for row in data[:]:
        if row[0]==access_key:
            for row_element in row:
                print(row_element, end=' ')
    print("\n")

def map_row(col_instance):
    try:
        col_instance=list(map(int, col_instance))
    except ValueError:
        col_instance=list(map(float, col_instance))

    return col_instance

def print_row(col_instance):
    for row_element in col_instance:
        print(row_element)

def sum(col_instance):
    sum=0
    for row_element in col_instance:
        sum+=row_element

    return sum

def avg(col_instance):
    avg=sum(col_instance)/len(col_instance)
    return avg

def maximum(col_instance):
    maximum=col_instance[0]
    for row_element in col_instance:
        if maximum < row_element:
            maximum = row_element

    return maximum

def minimum(col_instance):
    minimum=col_instance[0]
    for row_element in col_instance:
        if minimum > row_element:
            minimum = row_element

    return minimum

def deviation(col_instance):
    deviation=[]
    for row_element in col_instance:
        deviation.append(row_element-avg(col_instance))

    return deviation

def variance(col_instance):
    sum=0
    for dev_element in deviation(col_instance):
        sum+=dev_element*dev_element
        variance=sum/len(deviation(col_instance))

    return variance

def standard_deviation(col_instance):
    standard_deviation=math.sqrt(variance(col_instance))

    return standard_deviation

def ascend(col_instance):
    ascend=sorted(col_instance)
    for asc in ascend:
        print(asc)

def descend(col_instance):
    descend=reversed(sorted((col_instance)))
    for desc in descend:
        print(desc)


with open('Demographic_Statistics_By_Zip_Code.csv', newline='') as infile:
    data=list(csv.reader(infile))

while True:
    input_num=input("0.종료 1.행 2.열 3.총합 4.평균 5.최대값 6.최소값 7.편차 8.분산 9.표준편차 10.오름차순 정렬 11.내림차순 정렬\n메뉴를 선택하세요: ")
    if input_num=='0': #0인 조건을 따로 분리하는 것을 추천
        break

    access_key=input("Access Key를 입력하세요: ")

    if input_num=='1':
        get_cvs_rowInstance(access_key)

    elif input_num=='2':
        print_row(map_row(get_cvs_colInstance(access_key)))
        print()

    elif input_num=='3':
        print_row(map_row(get_cvs_colInstance(access_key)))
        print("총합: "+str(sum(map_row(get_cvs_colInstance(access_key))))+"\n")

    elif input_num=='4':
        print_row(map_row(get_cvs_colInstance(access_key)))
        print("평균: "+str(avg(map_row(get_cvs_colInstance(access_key))))+"\n")

    elif input_num=='5':
        print_row(map_row(get_cvs_colInstance(access_key)))
        print("최대값: "+str(maximum(map_row(get_cvs_colInstance(access_key))))+"\n")

    elif input_num=='6':
        print_row(map_row(get_cvs_colInstance(access_key)))
        print("최소값: "+str(minimum(map_row(get_cvs_colInstance(access_key))))+"\n")

    elif input_num=='7':
        for row in range(0,len(map_row(get_cvs_colInstance(access_key)))):
            print(str(map_row(get_cvs_colInstance(access_key))[row])+"   \t\t"+str(deviation(map_row(get_cvs_colInstance(access_key)))[row]))
        print("편차 = 표본 - 평균\n")

    elif input_num=='8':
        print_row(map_row(get_cvs_colInstance(access_key)))
        print("분산 (공식: (∑(표본-평균)^2)/표본수): "+str(variance(map_row(get_cvs_colInstance(access_key))))+"\n")

    elif input_num=='9':
        print_row(map_row(get_cvs_colInstance(access_key)))
        print("표준편차 (공식: √분산): "+str(standard_deviation(map_row(get_cvs_colInstance(access_key))))+"\n")

    elif input_num=='10':
        ascend(map_row(get_cvs_colInstance(access_key))+"\n")

    elif input_num=='11':
        descend(map_row(get_cvs_colInstance(access_key))+"\n")