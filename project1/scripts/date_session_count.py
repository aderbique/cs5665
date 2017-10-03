#!/user/bin/python3

#Austin Derbique
#A01967241
#9/12/17
#CS5460 Data Science: Assignment 3

import sys, re, csv

dictionary = {}

regex = """(\d*\.\d*\.\d*\.\d*).*\[(\d\d)\/(\S*)\/(\d*)\:(\d*\:\d*\:\d*)\s\-(\d*)\]\s\"(\S\S\S)\s(.*)\"\s(\d\d\d)\s(.*)\s\"(.*)\"\s\"(.*)\""""
pat = re.compile(regex)
#group 1 = IP Address
#group 2 = Day
#group 3 = Month
#group 4 = Year
#group 5 = Time
#group 6 = Timezone
#group 7 = Action Type
#group 8 = Content location
#group 9 = Error Type
#group 10 = Something I'm not sure
#group 11 = website
#group 12 = device information

with open("mobile_access.log") as file:
    for line in file:
        m = pat.search(line)
        if m:
            month = m.group(3)
            if month == 'Jan': month = '1'
            elif month == 'Feb': month = '2'
            elif month == 'Mar': month = '3'
            elif month == 'Apr': month = '4'
            elif month == 'May': month = '5'
            elif month == 'Jun': month = '6'
            elif month == 'Jul': month = '7'
            elif month == 'Aug': month = '8'
            elif month == 'Sep': month = '9'
            elif month == 'Oct': month = '10'
            elif month == 'Nov': month = '11'
            elif month == 'Dec': month = '12'
            else: month = 'NULL'
            date = month + "/" + m.group(2) + "/" + m.group(4)
            if date in dictionary:
                dictionary[date] += 1
            else:
                dictionary[date] = 1

file.close()

w = csv.writer(open("mobile_sessions.csv", "w"))
count = 1
for key, val in sorted(dictionary.items()):
    w.writerow([key, val])
    count += 1
