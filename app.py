from flask import Flask
from flask import flash, redirect, request, jsonify
from flask_cors import CORS, cross_origin
import sys
import json
import requests

# app.py 
# Author: Clay Brimm
# 1/10/19

# Create app that has cross origin capabilities
app = Flask(__name__)
CORS(app)

# POST call that sends a json with latitude and longitude
@app.route('/weather', methods = ['POST'])
@cross_origin()
def api_weather():
	if request.method == 'POST':
		# Load json and assign lat and long variables
		data = json.dumps(request.json)
		recieved_data = json.loads(data)
		longitude = recieved_data["longitude"]
		latitude = recieved_data["latitude"]

		#GET request to the DarkSky API that sends a latitude and longitude
		response = requests.get("https://api.darksky.net/forecast/5e11ee3f5462123fa51ca228606b9839/"+latitude+","+longitude)

		#Create a JSON Object that has all the specific data that is necessary for the web app
		post_response = {}
		post_response["temperature"] = round(response.json()["currently"]["temperature"])
		post_response["summary"] = response.json()["currently"]["summary"]
		post_response["temperatureHigh"] = round(response.json()["daily"]["data"][0]["temperatureHigh"])
		post_response["temperatureLow"] = round(response.json()["daily"]["data"][0]["temperatureLow"])
		post_response["temperatureMax"] = round(response.json()["daily"]["data"][0]["temperatureMax"])
		post_response["precipProbability"] = round(response.json()["daily"]["data"][0]["precipProbability"] * 100)
		
		#Some locations do not have available precipTypes
		try:
			post_response["precipType"] = response.json()["daily"]["data"][0]["precipType"]
		except:
			print("Location does not have precipitation type available.")
			post_response["precipType"] = "Not Available"

		post_response["windSpeed"] = response.json()["currently"]["windSpeed"]
		post_response["hourly"] = response.json()["hourly"]
		
		#Send back the JSON object as the response from the POST request
		return post_response
	else:
		return "THERE WAS A POST ERROR"


@app.errorhandler(400)
def not_found(error):
	return (jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run()