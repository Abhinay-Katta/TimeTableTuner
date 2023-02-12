import json
from clean_data import clean_TT
import pandas
import os
dff = pandas.read_excel(
    'tt.xlsx', sheet_name='6B4_AI')
new_dff = clean_TT(dff)
json_string = new_dff.to_json(orient="records")
folder_path = os.path.join(os.sep, 'D:\Projects\TT\json')

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

file_path = os.path.join(folder_path, "json_tt.json")
def take_div_num_to_create_json():


with open(file_path, "a") as file:
    file.write(json_string)
