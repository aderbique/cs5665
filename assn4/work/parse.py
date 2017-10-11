######################
# p3.py
######################

# We will use the request package to make http requests.
import requests

# Request a weather forecast from the National Weather Services National Digital Forecast Database (NDFD) via their REST API.
# See: https://www.weather.gov/mdl/ndfd_home
# See: https://www.weather.gov/mdl/ndfd_data_point
# See: https://graphical.weather.gov/xml/rest.php
weatherXML = requests.get("http://www.wrh.noaa.gov/mesowest/getobextXml.php?sid=DMHSD&num=72").text


# We will use ElementTree to parse the XML
import xml.etree.ElementTree as ET

# Initialize an ElementTree
root = ET.fromstring(weatherXML)

       

for sample in root.findall('ob'):
    time = sample.get('utime')
    for temp in sample:
        temperature = temp.attrib['value']
        print time + ',' + temperature
        break
    
    #temp = sample.find('T')
    #print time + ',' + temp
