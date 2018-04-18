import sys
import Adafruit_DHT
from function import upload
import uuid

print('Please Enter GPIO')
pin = input()

print('Please Enter username')
user = raw_input()

# make a random UUID
ID = uuid.uuid4()

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.AM2302

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Un-comment the line below to convert the temperature to Fahrenheit.
# temperature = temperature * 9/5.0 + 32

#Static Moisture
Moisture = 0

#Send to webserver
returncode = upload(user,ID,Moisture,temperature,humidity)

print(returncode)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
if humidity is not None and temperature is not None:
	#'{0:1.2f}'.format(5.555)  #returns '5.55'
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)
