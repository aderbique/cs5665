import sys, re, csv


regex = """(\d*\.\d*\.\d*\.\d*).*\[(\d\d)\/(\S*)\/(\d*)\:(\d*\:\d*\:\d*)\s\-(\d*)\]\s\"(\S\S\S)\s(.*)\"\s(\d\d\d)\s(.*)\s\"(.*)\"\s\"(.*)\""""

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



with open("access.log") as file:
    with open('tabulated.csv', 'w') as csvfile:
        fieldnames = ['IP Address', 'Day','Month','Year','Time','Time Zone','Action','Content Location','Error Code','idk','website','device info']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for line in file:
            m = re.search(regex, line)
            if m:
                month = m.group(3)
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
                writer.writerow({'IP Address' : m.group(1), 'Day' : m.group(2),'Month' : m.group(3),'Year' : m.group(4),'Time': m.group(5),'Time Zone' : m.group(6),'Action' : m.group(7) ,'Content Location' : m.group(8),'Error Code' : m.group(9),'idk' : m.group(10),'website' : m.group(11),'device info' : m.group(12)})
        csvfile.close()
    file.close()

