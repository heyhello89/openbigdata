import csv

def get_cvs_colInstance(col_name):
    col_instance=[]

    col_index=data[0].index(col_name)

    for row in data[1:]:
        col_instance.append(row[col_index])

    return col_instance

def print_row(col_instance, type="int"):
    if type == "int":
        list(map(int, col_instance))
    elif type == "float":
        list(map(float, col_instance))

    for row_element in col_instance:
        print(row_element)

def print_clo(row_instance):
    for row_element in row_instance:
        print(row_element, end=' ')


with open('Demographic_Statistics_By_Zip_Code.csv', newline='') as infile:
    data=list(csv.reader(infile))

# print_row(get_cvs_colInstance("COUNT FEMALE"))
print_row(get_cvs_colInstance("PERCENT FEMALE"), "float")
print_clo(data[2])
