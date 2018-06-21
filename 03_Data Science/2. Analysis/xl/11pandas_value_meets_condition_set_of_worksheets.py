import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, sheet_name=None, index_col=None)

column_output = []
for worksheets_name, data in data_frame.items():
    column_output.append(data.loc[:, ['Customer Name','Sale Amount']])
filtered_rows = pd.concat(column_output, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
filtered_rows.to_excel(writer, sheet_name='selected_columns_all_worksheets', index=False)
writer.save()