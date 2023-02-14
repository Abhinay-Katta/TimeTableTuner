import datetime
import json
import sys
import os
sys.path.append('../')


def schedule():
    folder = '../app/json'
    filename = 'jsontt_4.json'
    filepath = os.path.join(folder, filename)
    with open(filepath) as f:
        data = json.load(f)
    now = datetime.datetime.now()
    day = now.strftime("%A").upper()  # day done
    # time = now.strftime("%H:%M")
    time = '02:12'
    print(time)
    for i in data:
        time_range = i.get("Time")
        start_time, end_time = time_range.split(" - ")
        if start_time <= time <= end_time:
            print(i.get(day))
    if (time > end_time):
        print(time)
        print(end_time)
        print("Classes over")
        # if (day in i.keys()):
        #     print(i.get(day))  # whole day schedule


schedule()

# current_time=datetime.datetime.now().time()
# print(current_time)
# start_time=datetime.time(hour=21)
# end_time=datetime.time(hour=22)

#     print("The current time is between 11:00 and 12:00.")
# else:
#     print("The current time is not between 11:00 and 12:00.")
