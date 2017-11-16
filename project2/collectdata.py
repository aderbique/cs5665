#!/usr/bin/python


######################
# GetNDFDWeatherForPlace.py
######################

import sys, time, datetime

# sys.argv is the list of command-line arguments
# sys.arg[0] is the name of the program itself
# sys.arg[1] will be the latitude
# sys.arg[2] will be the longitude
# sys.arg[3] will be the place name

# set input and regular expression based on number of arguments

#datetime.date.strftime()

#print datetime.datetime.now().strftime("%Y%m%d%H%M")


if True is True:
	#strlat = sys.argv[1]
	#strlon = sys.argv[2]
        #strplacename = sys.argv[3]
	strlat = "32.99"
	strlon = "-117.16"
	strplacename = "San Diego"
	try:
		lat = float(strlat)
	except ValueError:
		print "Latitude must be specified as a floating point number."
		sys.exit()
	try:
		lon = float(strlon)
	except ValueError:
		print "Longitude must be specified as a floating point number."
		sys.exit()
# show USAGE message if wrong number of arguments
else:
	print "USAGE: python GetNDFDWeatherForPlace latitude longitude placename"
	sys.exit()
	
# We will use the request package to make http requests.
import requests

# Request a weather forecast from the National Weather Services National Digital Forecast Database (NDFD) via their REST API.
# See: https://www.weather.gov/mdl/ndfd_home
# See: https://www.weather.gov/mdl/ndfd_data_point
# See: https://graphical.weather.gov/xml/rest.php
#requeststr = "https://graphical.weather.gov/xml/sample_products/browser_interface/ndfdXMLclient.php?lat=" + strlat + "&lon=" + strlon + "&product=time-series&maxt=maxt&mint=mint&icons=icons&wx=wx"
requeststr = "https://graphical.weather.gov/xml/sample_products/browser_interface/ndfdXMLclient.php?lat=" + strlat + "&lon=" + strlon + "&product=time-series&temp=temp&maxt=maxt&mint=mint"
weatherstr = "http://www.wrh.noaa.gov/mesowest/getobextXml.php?sid=KMYF&num=72"

weatherXML = requests.get(requeststr).text
fn = "/home/ec2-user/cs5665/project2/temperature/" + datetime.datetime.now().strftime("%Y%m%d%H%M") + "_temp.xml"
file_handle = open(fn,"wb")
file_handle.write(weatherXML)
file_handle.close()

weatherXML = requests.get(weatherstr).text
fn = "/home/ec2-user/cs5665/project2/weather/" + datetime.datetime.now().strftime("%Y%m%d%H%M") + "_weather.xml"
file_handle = open(fn,"wb")
file_handle.write(weatherXML)
file_handle.close()



