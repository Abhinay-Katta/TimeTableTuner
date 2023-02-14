from flask import Flask, render_template, request
<<<<<<< HEAD
=======
import pandas
import os
>>>>>>> b0623ad29a74fdb1e89afa4a1b40011ebc6dc131
import sys
sys.path.append('./')
sys.path.append('../')

<<<<<<< HEAD
=======
# reading data:


def read_data(num):
    sheetname = '6B'+str(num)+'_AI'
    df = pandas.read_excel('./tt.xlsx', sheet_name=sheetname)
    print("data created")
    return clean_TT(df)


# cleaning data:


def clean_TT(df1):
    df1 = df1.drop(columns=["Unnamed: 0", "Unnamed: 7",
                            "Unnamed: 8", "Unnamed: 9"], )
    drop_these = []
    shape = df1.shape
    for i in range(0, shape[0]):
        if (i > 3 and i < 13):
            continue
        drop_these.append(i)
    df1 = df1.drop(drop_these)
    df1 = df1.reset_index(drop=True)
    cols = df1.iloc[0, :]
    df1.columns = cols
    df1 = df1.drop(0)
    df1 = df1.reset_index()
    df1 = df1.drop(columns='index')
    df1.iloc[2, :] = df1.iloc[2, :].fillna('RECESS')
    df1.iloc[5, :] = df1.iloc[5, :].fillna('RECESS')
    df1.fillna(method='ffill', inplace=True)
    df1.iloc[4, 0] = '01:50 - 02:40'
    print("data cleaned")
    return df1

# create json


def create_json_datafile(data, sheetname):
    folder = '../app/json/'
    filename = 'jsontt_'+str(sheetname)+'.json'
    filepath = os.path.join(folder, filename)
    # check if the folder exists or not, create one if it doesnt
    if not os.path.exists(folder):
        os.makedirs(folder)

    print(filename)
    print(filepath)
    json_string = data.to_json(orient="records")
    with open(filepath, 'w') as json:
        json.write(json_string)


# find correct schedule:
def print_schedule():
    schedule = 'asd'
    return schedule
    # TODO: send correct schedule based on time, class, div


    # main:
>>>>>>> b0623ad29a74fdb1e89afa4a1b40011ebc6dc131
app = Flask(__name__,
            static_folder='../static',
            template_folder='../templates')


@ app.route('/')
def index():
    return render_template('index.html', title='TT')


<<<<<<< HEAD
@app.route('/return_json_data', methods=['POST'])
def return_json_data():
    from create_json import take_div_num_to_create_json
    value = request.form.get('value')
    json_data = take_div_num_to_create_json(value)
    # do something with the value
    return render_template('rendon_json.html', json=json_data)
=======
@ app.route('/return_json_data', methods=['POST'])
def return_json_data():
    value = request.form.get('value')
    tt_data = read_data(value)
    create_json_datafile(tt_data, value)

    return str(print_schedule())
# test:
# value = 5
# print(value)
# print(tt_data)
# print(create_json_datafile)
>>>>>>> b0623ad29a74fdb1e89afa4a1b40011ebc6dc131


if __name__ == '__main__':
    app.run()
