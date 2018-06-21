import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)

important_dates = ['01/24/2013', '01/31/2013']
data_frame_value_meets_condition = data_frame[data_frame['Customer Name'].str.startswith("J")]

writer = pd.ExcelWriter(output_file)
data_frame_value_meets_condition.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()