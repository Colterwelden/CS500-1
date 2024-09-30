hours = [i for i in range(24)]
current_time = int(input("What is the current time: "))
time_to_alarm = int(input("In how many hours do you wish the alarm to sound:" ))
alarm_time = (current_time + time_to_alarm) % 24
print(f"The alarm will go off at: {hours[alarm_time]}:00")
input("Press Enter to close...")