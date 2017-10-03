#!/user/bin/python3

#Austin Derbique
#A01967241
#9/12/17
#CS5460 Data Science: Assignment 3

import sys, re, argparse, csv

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

dictionary = {}

regex = "\[\w\w\w\s(\w\w\w)\s(\d\d).*.(\d\d\d\d)]\s\[(.*)]\s\[client.(.*)].(.*)"
with open(args.filename) as file:
    for line in file:
        m = re.search(regex, line)
        if m:
            month = m.group(1)
            if month == 'Jan': month = '01'
            elif month == 'Feb': month = '02'
            elif month == 'Mar': month = '03'
            elif month == 'Apr': month = '04'
            elif month == 'May': month = '05'
            elif month == 'Jun': month = '06'
            elif month == 'Jul': month = '07'
            elif month == 'Aug': month = '08'
            elif month == 'Sep': month = '09'
            elif month == 'Oct': month = '10'
            elif month == 'Nov': month = '11'
            elif month == 'Dec': month = '12'
            else: month = 'NULL'
            date = m.group(3) + month + m.group(2)
            if date in dictionary:
                dictionary[date] += 1
            else:
                dictionary[date] = 1
file.close()

w = csv.writer(open("datecount.csv", "w"))
count = 1
for key, val in sorted(dictionary.items()):
    w.writerow([key, count, val])
    count += 1
