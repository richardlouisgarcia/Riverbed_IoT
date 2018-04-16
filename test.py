from function import upload
import uuid

#print('Please Enter Sensor ID')
#ID= input()

# make a random UUID
ID = uuid.uuid4()
print(ID)

print('Please Enter Moisture')
Moisture = input()

print('Please Enter Temperature')
degreeC = input()

print('Please Enter Humidity')
humidity = input()

returncode = upload(ID,Moisture,degreeC,humidity)

print(returncode)
