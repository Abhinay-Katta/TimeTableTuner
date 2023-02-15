import time
import datetime
import json
import sys
import os
sys.path.append('../')


# Get the current time
current_time = time.localtime()

# Format the hours in 12-hour format
formatted_time = time.strftime("%I:%M", current_time)

# Print the formatted time
print(formatted_time)


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
    print(time)
    if (int(time.split(':'))[0] > 12):
        hr = now.strftime('%H')
        print(hr-12)
        # time.replace(int(time.split(':')[0]), int(time.split(':')[0]) -= 12)
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


# schedule(4)
