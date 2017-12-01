# We will use ElementTree to parse the XML
import xml.etree.ElementTree as ET
import collections
from decimal import *

#max_temps = {"0Date": ["0 day","1 day","2 day","3 day",'4 day','5 day','6 day']}
#min_temps = {"0Date": ["0 day","1 day","2 day","3 day",'4 day','5 day','6 day']}

max_temps = {}
min_temps = {}

for x in range(16,30):
  #print "X is: " + str(x)
  fn = "201711" + str(x) + "0000_temp.xml"
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
	    
	    
	mins = params.findall("[@type='minimum']")
	for val in mins:
	  min_list = []
	  min_count = 0
	  for vals in val.findall('value'):
	    #print vals.text
	    key = "201711" + str(x + min_count)
	    if key not in min_temps:
	       min_temps[key] = [0,0,0,0,0,0,0]
	    list_of_temps = min_temps[key]
	    list_of_temps[min_count] = int(vals.text)
	    min_temps[key] = list_of_temps
	    min_count = min_count + 1    
	    
	    
	    
	    
	  #maximum = temp.findall("[@type='maximum']")
	  #print maximum.text
    #print "iterating through temps"
    #if temps.get['type'] == "maximum":
    #  print "max found!"
    #  for maxes in temps:
#	maximum = temps.attrib['value']
#	print maximum
print "Minimum temperatures"
print "\nDate, d0, d1, d2, d3, d4 ,d5, d6"
min_od = collections.OrderedDict(sorted(min_temps.items()))
for days in min_od:
  print days, min_od[days]

print "\nMaximum Temperatures"
print "\nDate, d0, d1, d2, d3, d4 ,d5, d6"
max_od = collections.OrderedDict(sorted(max_temps.items()))
for days in max_od:
  print days, max_od[days]
  
  
  
  
#days 22 through 29 have full data so we will test errors on those

new_min_od = {}
for days in min_od:
  if int(days) in range(20171122,20171130):
    alist = min_od[days]
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
    new_min_od[days] = alist    
    
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

print "\nMinimum errors for 1 day prediction, 6 day prediction, and overall error."
print "\nDate, d0, d1, d2, d3, d4 ,d5, d6, e1, e2, e3, e4, e5, e6, eO"
new_min_od = collections.OrderedDict(sorted(new_min_od.items()))
for days in new_min_od:
  print days, new_min_od[days]    

print "\nMaximum Errors for 1 day prediction, 6 day prediction, and overall error."
print "\nDate, d0, d1, d2, d3, d4 ,d5, d6, e1, e2, e3, e4, e5, e6, eO"
new_max_od = collections.OrderedDict(sorted(new_max_od.items()))
for days in new_max_od:
  print days, new_max_od[days]


       
"""
for sample in root.findall('ob'):
    time = sample.get('utime')
    for temp in sample:
        temperature = temp.attrib['value']
        print time +  ',' + temperature
        break 
"""