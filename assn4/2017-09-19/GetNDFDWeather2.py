######################
# GetNDFDWeather2.py
######################

# We will use the request package to make http requests.
import requests

# Request a weather forecast from the National Weather Services National Digital Forecast Database (NDFD) via their REST API.
# See: https://www.weather.gov/mdl/ndfd_home
# See: https://www.weather.gov/mdl/ndfd_data_point
# See: https://graphical.weather.gov/xml/rest.php
weatherXML = requests.get("https://graphical.weather.gov/xml/sample_products/browser_interface/ndfdXMLclient.php?lat=41.74&lon=-111.83&product=time-series&maxt=maxt&mint=mint").text

# We will use ElementTree to parse the XML
import xml.etree.ElementTree as ET

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
		starttimes.append(starttimeelement.text)
	# Retrieve and store the start times as a list.
	endtimes = []
	for endtimeelement in timelayoutelement.findall("end-valid-time"):
		endtimes.append(endtimeelement.text)
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
	# Retrieve and store the values as a list.
	parametervalues = []
	for value in parameterelement.findall("value"):
		parametervalues.append(value.text)
	# Store in the weatherparameters dictionary.
	weatherparameters[parameterelementname] = {"tag" : parameterelementtag , "attribs" : parameterelementattribs , "values" : parametervalues}
	
# Print it all out - messy.
for weatherparametername in weatherparameters:
	# Organize by weather parameter name.
	print weatherparametername
	# Get the time layout, to match with the values.
	timelayout = weatherparameters[weatherparametername]["attribs"]["time-layout"]
	# Units should be displayed as well.
	units = weatherparameters[weatherparametername]["attribs"]["units"]
	# Get the values.
	values = weatherparameters[weatherparametername]["values"]
	# Iterate through the values and print accordingly to include the time range, value and units.
	for x in range(0,len(values)-1):
		print timelayouts[timelayout][0][x], timelayouts[timelayout][1][x], values[x], units