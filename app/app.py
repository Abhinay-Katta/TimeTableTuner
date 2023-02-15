from flask import Flask, render_template, request
import pandas
import os
import sys
sys.path.append('./')
sys.path.append('../')

# reading data:


def read_data(num):
    sheetname = '6B'+str(num)+'_AI'
    df = pandas.read_excel('./tt.xlsx', sheet_name=sheetname)
    # print("data created")
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
# REMOVED PART:
    # df1.columns = df1.columns.str.replace('(online)', '')
    # df1.columns = df1.columns.str.replace(' ', '')
    # df1.columns = df1.columns.str.replace('Y()', 'Y')
# REASON:
    # STRING FIX WAS NOT WORKING, SO JUST HAD TO REPLACE THAT WITH THE FOLLOWING:
    # INCREASES WORKLOAD BUT DOES WORK:
    df1.rename(columns={df1.columns[0]: "Time"}, inplace=True)
    df1.rename(columns={df1.columns[1]: "MONDAY"}, inplace=True)
    df1.rename(columns={df1.columns[2]: "TUESDAY"}, inplace=True)
    df1.rename(columns={df1.columns[3]: "WEDNESDAY"}, inplace=True)
    df1.rename(columns={df1.columns[4]: "THURSDAY"}, inplace=True)
    df1.rename(columns={df1.columns[5]: "FRIDAY"}, inplace=True)
    # print("data cleaned")
    return df1

# create json


def create_json_datafile(data, sheetname):
    folder = '../app/json/'
    filename = 'jsontt_'+str(sheetname)+'.json'
    filepath = os.path.join(folder, filename)
    # check if the folder exists or not, create one if it doesnt
    if not os.path.exists(folder):
        os.makedirs(folder)
    # print(filename)
    # print(filepath)
    json_string = data.to_json(orient="records")
    with open(filepath, 'w') as json:
        json.write(json_string)
        json.close()


# find correct schedule:

def schedule(sheetname):
    import json
    from flask import jsonify
    import datetime
    folder = '../app/json'
    filename = 'jsontt_'+str(sheetname)+'.json'
    filepath = os.path.join(folder, filename)
    with open(filepath) as f:
        data = json.load(f)
    now = datetime.datetime.now()
    day = now.strftime("%A").upper()
    time = now.strftime("%H:%M")
    # print(time)
    if (day == 'SUNDAY' or day == 'SATURDAY'):
        current_class = previous_class = next_class = 'no classes today'
    else:
        for index, i in enumerate(data):
            time_range = i.get("Time")
            start_time, end_time = time_range.split(" - ")
            # print(start_time, end_time)
            # print('\n')
            if (time < '10:00'):
                current_class = previous_class = next_class = "classes have not started yet"
            elif (time > end_time):
                current_class = previous_class = next_class = "classes ended for today"
            elif start_time <= time <= end_time:
                current_class = i.get(day)
                if index > 0:
                    previous_class = data[index-1].get(day)
                else:
                    previous_class = 'first class'
            # Search for next item in the loop
                if index < len(data)-1:
                    next_class = data[index+1].get(day)
                else:
                    next_class = 'last class'
            else:
                current_class = previous_class = next_class = 'something went wrong'
    response = [day.lower(), time, current_class, previous_class, next_class]
    # print(response)
    return response


    # main:
app = Flask(__name__,
            static_folder='../static',
            template_folder='../html')


@ app.route('/')
def index():
    return render_template('index.html', title='TT')


@ app.route('/return_json_data', methods=['POST'])
def return_json_data():
    value = request.form.get('value')
    tt_data = read_data(value)
    create_json_datafile(tt_data, value)
    return schedule(value)


if __name__ == '__main__':
    app.run()
