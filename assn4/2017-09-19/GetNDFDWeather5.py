######################
# GetNDFDWeather5.py
######################

# We will use the request package to make http requests.
import requests

# Request a weather forecast from the National Weather Services National Digital Forecast Database (NDFD) via their REST API.
# See: https://www.weather.gov/mdl/ndfd_home
# See: https://www.weather.gov/mdl/ndfd_data_point
# See: https://graphical.weather.gov/xml/rest.php
weatherXML = requests.get("https://graphical.weather.gov/xml/sample_products/browser_interface/ndfdXMLclient.php?lat=41.74&lon=-111.83&product=time-series&maxt=maxt&mint=mint&icons=icons").text

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
	

# The following somewhat convoluted approach prints out the forecast items in chronological order.
# Reference the maximum temperature data.
maxtemps = 	weatherparameters["Daily Maximum Temperature"]
# Reference the minimum temperature data.
mintemps = 	weatherparameters["Daily Minimum Temperature"]
# Reference the icon links.
icons = weatherparameters["Conditions Icons"]

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
	forecasts.append({"daystr" : WeatherDayString(timelayouts[timelayout][0][x]) , "valueandunits" : values[x] + " &deg;F" , "icon" : GetWeatherIconForTime(timelayouts[timelayout][0][x], icons)})

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
print "<table>"
print "<tr>"
for forecast in forecasts:
	print "<td>"
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
	print "<td>"
	print forecast["valueandunits"]
	print "</td>"
print "</tr>"
print "</table>"	
print "</body>"	
print "</html>"	
