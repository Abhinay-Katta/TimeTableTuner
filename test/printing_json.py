import datetime
import json
import sys
import os

sys.path.append('../')
folder = '../app/json'
# example:
filename = 'jsontt_4.json'
filepath = os.path.join(folder, filename)

with open(filepath) as f:
    data = json.load(f)
print(data[2].get('Time'))
# Get the current day and time
now = datetime.datetime.now()
day = now.strftime("%A").upper()
time = now.strftime("%H:%M")
print(data[2].get(day))

# output:
# print(data[i].get(day)) where i is the current time object

print(now, day, time)
print(str(day))

for i in data:
    with open('txt.txt', 'a') as d:
        d.write(str(i))
    d.close()
    print(i.keys())
    print('\n')
    print('\n')
    print('\n')

    print(i.values())
    print('\n')
    print('\n')
    print('\n')

    print(i.get(day))

    if (i.keys() == str(day)):
        print(i.get(day))


# data[2]

# # Loop through the schedule to find the current class
# current_class = None
# for period in data:
#     timing = period["DAY\nTIMING              "].split()
#     if len(timing) >= 4 and timing[1] <= time < timing[3]:
#         if day in period:
#             current_class = period[day]
#             break

# # Print the current class, or a message if there is no current class
# if current_class:
#     print(current_class)
# else:
#     print("There is no current class at this time.")
