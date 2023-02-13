from cleaner import clean_data
import pandas
import sys
inputt = sys.argv[1]
sheet_namee = '6B'+inputt+'_AI'
dff = pandas.read_excel('./6th_Divsion_TT.xlsx', sheet_name=sheet_namee)


ss = str((clean_data.clean_TT(dff)))
print(ss)
with open('new.txt', 'a') as sss:
    sss.write(ss)
