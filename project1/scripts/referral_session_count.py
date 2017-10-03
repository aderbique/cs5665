#!/user/bin/python3

#Austin Derbique
#A01967241
#9/12/17
#CS5460 Data Science: Assignment 3

import sys, re, csv

dictionary = {}

regex = "http://www\.([^/]*)"
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

with open("desktop_access.log") as file:
    for line in file:
        m = pat.search(line)
        if m:
            
            if m.group(1) in dictionary:
                dictionary[m.group(1)] += 1
            else:
                dictionary[m.group(1)] = 1

file.close()

w = csv.writer(open("desktop_referrals.csv", "w"))
count = 1
for key, val in sorted(dictionary.items()):
    w.writerow([key, val])
    count += 1
