import csv
import glob
import os
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple

item_numbers_file = sys.argv[1]
path_to_folder = sys.argv[2]
output_file = sys.argv[3]

item_numbers_to_find = []
with open(item_numbers_file, 'r', newline='') as item_numbers_csv_file:
    filereader = csv.reader(item_numbers_csv_file)
    for row in filereader:
        item_numbers_to_find.append(row[0])
print(item_numbers_to_find)

filewriter = csv.writer(open(output_file, 'a', newline=''))

file_counter = 0
line_counter = 0
count_of_item_numbers = 0
for input_file in glob.glob(os.path.join(path_to_folder, '*.*')):
    file_counter += 1
    if input_file.split('.')[1] == 'csv':
        with open(input_file, 'r', newline='') as csv_in_file:
            filereader = csv.reader(csv_in_file)
            header = next(filereader)
            for row in filereader:
                row_of_output = []
                for column in range(len(header)):
                    if column < 3:
                        cell_value = str(row[column]).strip()
                        row_of_output.append(cell_value)
                    elif column == 3:
                        cell_value = str(row[column]).lstrip('$').replace('.','').split('.')[0].strip()
                        row_of_output.append(cell_value)
