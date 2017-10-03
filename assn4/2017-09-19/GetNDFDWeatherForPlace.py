######################
# GetNDFDWeatherForPlace.py
######################

import sys

# sys.argv is the list of command-line arguments
# sys.arg[0] is the name of the program itself
# sys.arg[1] will be the latitude
# sys.arg[2] will be the longitude
# sys.arg[3] will be the place name

# set input and regular expression based on number of arguments



if True is True:
	#strlat = sys.argv[1]
	#strlon = sys.argv[2]
        #strplacename = sys.argv[3]
	strlat = "40.7"
	strlon = "-74.0"
	strplacename = "New York City"
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
requeststr = "https://graphical.weather.gov/xml/sample_products/browser_interface/ndfdXMLclient.php?lat=" + strlat + "&lon=" + strlon + "&product=time-series&maxt=maxt&mint=mint&icons=icons&wx=wx"
weatherXML = requests.get(requeststr).text

# We will use ElementTree to parse the XML
import xml.etree.ElementTree as ET
	
# We will use the following to parse the date strings.
from dateutil.parser import parse

# And this will be used to process date objects.
import datetime

# Returns a string representation of the day of week. If today, then return 
def WeatherDayString(timeobj):
	now = datetime.datetime.now()
	if now.year == timeobj.year and now.month == timeobj.month and now.day == timeobj.day:
		if timeobj.hour < 12:
			wxstr = 'Today'
		else:
			wxstr = 'Tonight'
	else:
		wxstr = timeobj.strftime("%A")
		if timeobj.hour >= 12:
			wxstr = wxstr + "<br>Night"
	#wxstr = wxstr + " (" + timeobj.strftime("%m-%d-%Y") + ")"
	return wxstr
	
def GetWeatherIconForTime(timeobj, icons):
	nearestindex = 0
	besttimediff = abs(timeobj - timelayouts[icons["attribs"]["time-layout"]][0][0])
	for x in range(1,len(icons["iconlinks"])-1):
		timediff = abs(timeobj - timelayouts[icons["attribs"]["time-layout"]][0][x])
		if (timediff < besttimediff):
			besttimediff = timediff
			nearestindex = x
	iconlinkstr = icons["iconlinks"][nearestindex]
	return iconlinkstr
	
def GetWeatherDescriptionForTime(timeobj, weatherdescriptions):
	nearestindex = 0
	besttimediff = abs(timeobj - timelayouts[weatherdescriptions["attribs"]["time-layout"]][0][0])
	for x in range(1,len(weatherdescriptions["weatherconditions"])-1):
		timediff = abs(timeobj - timelayouts[weatherdescriptions["attribs"]["time-layout"]][0][x])
		if (timediff < besttimediff):
			besttimediff = timediff
			nearestindex = x
	weatherdescriptionstr = weatherdescriptions["weatherconditions"][nearestindex]
	return weatherdescriptionstr


# Initialize an ElementTree
root = ET.fromstring(weatherXML)

# Extract the time layouts.
# We will store them in a dictionary for easy retrieval.
timelayouts = {}
# Use xpath to find the time-layout elements.
for timelayoutelement in root.findall("./data/time-layout"):
	# Get the layout key for each.
	layoutkey = timelayoutelement.find("layout-key").text
	# Retrieve and store the start times as a list.
	starttimes = []
	for starttimeelement in timelayoutelement.findall("start-valid-time"):
		starttimes.append(parse(starttimeelement.text))
	# Retrieve and store the start times as a list.
	endtimes = []
	for endtimeelement in timelayoutelement.findall("end-valid-time"):
		endtimes.append(parse(endtimeelement.text))
	# Store in the timelayouts dictionary.
	timelayouts[layoutkey] = [starttimes, endtimes]
	
# Extract the weather parameters
# We will store them in a dictionary for easy retrieval.
weatherparameters = {}
for parameterelement in root.find("./data/parameters/."):
	# The tag name is a short name for the type of weather element.
	parameterelementtag = parameterelement.tag
	# The attributes are returned as a dictionary.
	parameterelementattribs = parameterelement.attrib
	# This name is better for use than the tag name since it is unique.
	parameterelementname = parameterelement.find("name").text
	if parameterelementtag == "temperature":
		# Retrieve and store the values as a list.
		parametervalues = []
		for value in parameterelement.findall("value"):
			parametervalues.append(value.text)
		# Store in the weatherparameters dictionary.
		weatherparameters[parameterelementname] = {"tag" : parameterelementtag , "attribs" : parameterelementattribs , "values" : parametervalues}
	elif parameterelementtag == "conditions-icon":
		# Retrieve and store the values as a list.
		parametericonlinks = []
		for iconlink in parameterelement.findall("icon-link"):
			parametericonlinks.append(iconlink.text)
		# Store in the weatherparameters dictionary.
		weatherparameters[parameterelementname] = {"tag" : parameterelementtag , "attribs" : parameterelementattribs , "iconlinks" : parametericonlinks}	
	elif parameterelementtag == "weather":
		# Retrieve and store the values as a list.
		parameterweatherconditions = []
		for weathercondition in parameterelement.findall("weather-conditions"):
			weathervalue = weathercondition.find("value")
			if weathervalue is None:
				weatherstr = "clear"
			else:
				weatherstr = weathervalue.attrib["coverage"] + " " + weathervalue.attrib["intensity"] + " " + weathervalue.attrib["weather-type"]
			parameterweatherconditions.append(weatherstr)
		# Store in the weatherparameters dictionary.
		weatherparameters[parameterelementname] = {"tag" : parameterelementtag , "attribs" : parameterelementattribs , "weatherconditions" : parameterweatherconditions}	
	

# The following somewhat convoluted approach prints out the forecast items in chronological order.
# Reference the maximum temperature data.
maxtemps = 	weatherparameters["Daily Maximum Temperature"]
# Reference the minimum temperature data.
mintemps = 	weatherparameters["Daily Minimum Temperature"]
# Reference the icon links.
icons = weatherparameters["Conditions Icons"]
# Reference the weather text.
weather = weatherparameters["Weather Type, Coverage, and Intensity"]

xmaxindex = 0
xminindex = 0
# Check determines whether to start with a min or max temp.
if timelayouts[maxtemps["attribs"]["time-layout"]][0][0] < timelayouts[mintemps["attribs"]["time-layout"]][0][0]:
	maxnext = True
else:
	maxnext = False

# Loop through the temps, alternating between max and min to present them in chronological order.
forecasts = []
while xmaxindex<len(maxtemps["values"]) or xminindex<len(mintemps["values"]):
	if maxnext:
		wxparams = maxtemps
		x = xmaxindex
	else: 
		wxparams = mintemps
		x = xminindex

	# Get the time layout, to match with the values.
	timelayout = wxparams["attribs"]["time-layout"]
	# Units should be displayed as well.
	units = wxparams["attribs"]["units"]
	# Get the values.
	values = wxparams["values"]
		
	#print WeatherDayString(timelayouts[timelayout][0][x]), values[x], units, GetWeatherIconForTime(timelayouts[timelayout][0][x], icons)
	forecasts.append({"daystr" : WeatherDayString(timelayouts[timelayout][0][x]) , "valueandunits" : values[x] + " &deg;F" , "icon" : GetWeatherIconForTime(timelayouts[timelayout][0][x], icons) , "weatherdescription" : GetWeatherDescriptionForTime(timelayouts[timelayout][0][x], weather)})

	# Alternate for the next.
	if maxnext:
		xmaxindex = xmaxindex + 1
		if xminindex < len(mintemps["values"]):
			maxnext = False
		else:
			maxnext = True
	else: 
		xminindex = xminindex + 1
		if xmaxindex < len(maxtemps["values"]):
			maxnext = True
		else:
			maxnext = False

print "<html>"
print "<body>"
print "<h1>The Forecast for " + strplacename + " is:</h1>"
print "<table>"
print "<tr>"
for forecast in forecasts:
	print "<td valign=bottom>"
	print forecast["daystr"]
	print "</td>"
print "</tr>"
print "<tr>"
for forecast in forecasts:
	print "<td>"
	print "<img src=\"" + forecast["icon"] + "\">"
	print "</td>"
print "</tr>"
print "<tr>"
for forecast in forecasts:
	print "<td valign=top>"
	print forecast["weatherdescription"]
	print "</td>"
print "</tr>"
print "<tr>"
for forecast in forecasts:
	print "<td>"
	print forecast["valueandunits"]
	print "</td>"
print "</tr>"
print "</table>"	
print "</body>"	
print "</html>"	
