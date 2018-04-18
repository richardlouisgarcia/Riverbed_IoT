import requests
import json
from datetime import datetime
import time
#import geocoder #alternative GPS

def upload(user,UUID,Moisture,temp,humidity):
	
	#Convert UUID to string for JSON
	ID = str(UUID)
	
	#Get current date & time
	date = datetime.now().strftime("%x")
	timestamp = datetime.now().strftime("%X")
	
	#Get seconds since epoch convert to JSON
	#epoch = json.dumps(time.time())
	#Get miliseconds since epoch convert to JSON
	epoch = int(round(time.time() * 1000))
	
	#Get Location in GPS format to JSON
	geo_r = requests.get("http://freegeoip.net/json")
	geo_json = geo_r.json()
	GPS_tmp=[geo_json["latitude"],geo_json["longitude"]]
	GPS=json.dumps(GPS_tmp)

	#Alternative GPS
	#g = geocoder.ip('me')
	#GPS = g.latlng

	#Static GPS
	#GPS = '47.7157, -122.301'

	#Static API Key
	APIkey ='007'

	#Server Location
	#url ='http://52.191.135.88:8080/sensor'
	url ='http://40.70.0.179:8080/sensor'

	#Send Payload to Server
	#r = requests.post(url, json={"id":ID,"gps":GPS,"apikey":APIkey,"timestamp":TimeStamp,"sensordata": {"moisture":Moisture,"temp":temp,"humidity":humidity}})
	r = requests.post(url, json={"date":date,"epoch":epoch,"user":user,"timestamp":timestamp,"moisture":Moisture,"temp":temp,"humidity":humidity,"gps":GPS,"apikey":APIkey,"serial":ID})

	#Get status code and return to caller
	statuscode = r.status_code
	return statuscode
