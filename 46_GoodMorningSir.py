import time
timestamp = time.strftime('%H:%M,%S')
print(timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)
timestamp = int(time.strftime('%M'))
print(timestamp)
timestamp = int(time.strftime('%S'))
print(timestamp)

timestamp = int(time.strftime('%H'))

if 6 <= timestamp <= 12:
    print("Good Morning Sir!")

elif 12 <= timestamp <= 18:
    print("Good Afternoon Sir")

else:
    print("Good Evening Sir")
