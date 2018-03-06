from function import upload

print('Please Enter Sensor ID')
ID= input()

print('Please Enter Sensor Data')
SensorData = input()

returncode = upload(ID,SensorData)

print(returncode)