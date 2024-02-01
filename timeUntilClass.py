#!/usr/bin/env python3

from datetime import datetime, timedelta

class_schedule = [
    ("07:00:00", "07:50:00"),
    ("08:00:00", "08:50:00"),
    ("09:00:00", "09:50:00")
]

current_time = datetime.now().strftime('%H:%M:%S')

class_active = False
for start_time, end_time in class_schedule:
    if start_time <= current_time <= end_time:
        class_active = True
        end_time_obj = datetime.strptime(end_time, '%H:%M:%S')
        current_time_obj = datetime.strptime(current_time, '%H:%M:%S')
        remaining_time = end_time_obj - current_time_obj

        total_seconds = max(int(remaining_time.total_seconds()), 0)
        minutes, seconds = divmod(total_seconds, 60)
        formatted_remaining_time = '{:02}:{:02}'.format(minutes, seconds)

        print(formatted_remaining_time)

        break  # Exit the loop once we find the active class

if not class_active:
    next_class_start_time = datetime.strptime(class_schedule[0][0], '%H:%M:%S')

    # Calculate time to the next class
    for start_time, _ in class_schedule:
        if start_time >= current_time:
            next_class_start_time = datetime.strptime(start_time, '%H:%M:%S')
            break  # Exit the loop once we find the next class

    time_to_next_class = next_class_start_time - datetime.strptime(current_time, '%H:%M:%S')

    total_seconds = max(int(time_to_next_class.total_seconds()), 0)
    minutes, seconds = divmod(total_seconds, 60)
    formatted_time_to_next_class = '{:02}:{:02}'.format(minutes, seconds)
    
    if formatted_time_to_next_class == '00:00':
        print('')
    else:
        print(formatted_time_to_next_class)
