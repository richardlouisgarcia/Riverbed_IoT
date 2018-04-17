from function import upload
import uuid

print('Please Enter username')
user = input()

# make a random UUID
ID = uuid.uuid4()

print('Please Enter Moisture')
Moisture = input()

print('Please Enter Temperature')
temp = input()

print('Please Enter Humidity')
humidity = input()

returncode = upload(user,ID,Moisture,temp,humidity)

print(returncode)
