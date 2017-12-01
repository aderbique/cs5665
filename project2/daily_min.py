# We will use ElementTree to parse the XML
import xml.etree.ElementTree as ET


print "running"

daily_temp = {"Date": ["Min","1 day","2 day","3 day"]}

for x in range(16,30):
  fn = "201711" + str(x) + "0000_temp.xml"
  tree = ET.parse(fn)
  root = tree.getroot()
  for temps in root.findall('temperature'):
    if temps.get['type'] == "maximum":
      for maxes in temps:
	maximum = temps.attrib['value']
	print maximum
  

       
"""
for sample in root.findall('ob'):
    time = sample.get('utime')
    for temp in sample:
        temperature = temp.attrib['value']
        print time +  ',' + temperature
        break 
"""