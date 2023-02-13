from cleaner import clean_data
import os
num = 56
file_name = 'json_tt_'+str(num)+'.json'
folder = 'D:\\Projects\\TT\\json'


def create_file(file_name, folder):
    full_path = os.path.join(folder, file_name)
    if file_name in os.listdir(folder):
        return 0
    else:
        with open(full_path, 'a') as d:
            d.write(clean_data.clean_TT())
        return 'done'


print(create_file(file_name, folder))
