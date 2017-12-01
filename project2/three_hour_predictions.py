# We will use ElementTree to parse the XML
import xml.etree.ElementTree as ET
import collections
from decimal import *

#max_temps = {"0Date": ["0 day","1 day","2 day","3 day",'4 day','5 day','6 day']}
#min_temps = {"0Date": ["0 day","1 day","2 day","3 day",'4 day','5 day','6 day']}

inc = {}

#There are 112 hours in the span of the 16th - 30th
#We will start at 7pm

 yrmth = "201711"
 day = 15
 hour = 19
 minutes = "00"
  
for x in range(0,111):
  time_add = x * 3
  hour = hour + time_add
  if hour == 25:
    hour = 0
    day = day + 1
    
  if hour < 10:
    hour_string = "0" + str(hour)
  #print "X is: " + str(x)
  fn = yrmth + str(day) + hour_string + minutes + "_temp.xml"
  print fn
  tree = ET.parse(fn)
  root = tree.getroot()
  for head in root.findall('data'):
    for data in head:
      for params in data.findall('temperature'):
	#for temp in params:
	
	
	maxes = params.findall("[@type='maximum']")
	for val in maxes:
	  max_list = []
	  max_count = 0
	  for vals in val.findall('value'):
	    #print vals.text
	    key = "201711" + str(x + max_count)
	    if key not in max_temps:
	       max_temps[key] = [0,0,0,0,0,0,0]
	    list_of_temps = max_temps[key]
	    list_of_temps[max_count] = int(vals.text)
	    max_temps[key] = list_of_temps
	    max_count = max_count + 1
	    
	    
	   

#print "\nMaximum Temperatures"
#print "\nDate, d0, d1, d2, d3, d4 ,d5, d6"
#max_od = collections.OrderedDict(sorted(max_temps.items()))
#for days in max_od:
#  print days, max_od[days]
  
  
  
  
#days 22 through 29 have full data so we will test errors on those
"""    
new_max_od = {}
for days in max_od:
  if int(days) in range(20171122,20171130):
    alist = max_od[days]
    alist.append(round(abs(((alist[1] - 0.0 - alist[0])/alist[0])*100),2))
    alist.append(round(abs(((alist[2] - 0.0 - alist[0])/alist[0])*100),2))
    alist.append(round(abs(((alist[3] - 0.0 - alist[0])/alist[0])*100),2))
    alist.append(round(abs(((alist[4] - 0.0 - alist[0])/alist[0])*100),2))
    alist.append(round(abs(((alist[5] - 0.0 - alist[0])/alist[0])*100),2))
    alist.append(round(abs(((alist[6] - 0.0 - alist[0])/alist[0])*100),2))
    alist.append(round((alist[6] + alist[7] + alist[8] + alist[9] + alist[10] + alist[11])/6,2))
    #print "Error1 is: " + days, str(alist[7])
    #print "Error6 is: " + days, str(alist[12])
    #print "ErrorO is: " + days, str(alist[13])
    #errorall = (alist[1] + alist[2] + alist[3] + alist[4] + alist[5] + alist[6])/6
    new_max_od[days] = alist    

print "\nMaximum Errors for 1 day prediction, 6 day prediction, and overall error."
print "\nDate, d0, d1, d2, d3, d4 ,d5, d6, e1, e2, e3, e4, e5, e6, eO"
new_max_od = collections.OrderedDict(sorted(new_max_od.items()))
for days in new_max_od:
  print days, new_max_od[days]
"""
