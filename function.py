import requests
import json
import datetime
#import geocoder #alternative GPS

def upload(ID,Moisture,degreeC,humidity):
	#Get current UTC time and convert to iso format for JSON
	TimeStamp = datetime.datetime.utcnow().isoformat()
	
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
	#r = requests.post(url, json={"id":ID,"timeStamp":TimeStamp,"sensorData":SensorData,"gps":GPS,"apiKey":"12344"})
	r = requests.post(url, json={"id":ID,"gps":GPS,"apikey":APIkey,"timestamp":TimeStamp,"sensordata": {"moisture":Moisture,
	"temp":degreeC,"humidity":humidity}})

	#Get status code and return to caller
	statuscode = r.status_code
	return statuscode

#Error code
#returns none or error
#bad_r.raise_for_status() 
