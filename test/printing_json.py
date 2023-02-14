import datetime
import json
import sys
import os

sys.path.append('../')
folder = '../app/json'
filename = 'jsontt_4.json'
filepath = os.path.join(folder, filename)

with open(filepath) as f:
    data = json.load(f)

# Get the current day and time
now = datetime.datetime.now()
day = now.strftime("%A").upper()
time = now.strftime("%H:%M")

# Loop through the schedule to find the current class
current_class = None
for period in data:
    timing = period["DAY\nTIMING              "].split()
    if len(timing) >= 4 and timing[1] <= time < timing[3]:
        if day in period:
            current_class = period[day]
            break

# Print the current class, or a message if there is no current class
if current_class:
    print(current_class)
else:
    print("There is no current class at this time.")
