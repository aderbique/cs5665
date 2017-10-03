######################
# GetNDFDWeather1.py
######################

# We will use the request package to make http requests.
import requests

# Request a weather forecast from the National Weather Services National Digital Forecast Database (NDFD) via their REST API.
# See: https://www.weather.gov/mdl/ndfd_home
# See: https://www.weather.gov/mdl/ndfd_data_point
# See: https://graphical.weather.gov/xml/rest.php
weatherXML = requests.get("https://graphical.weather.gov/xml/sample_products/browser_interface/ndfdXMLclient.php?lat=41.74&lon=-111.83&product=time-series&maxt=maxt&mint=mint").text

# Print it out.
print weatherXML
