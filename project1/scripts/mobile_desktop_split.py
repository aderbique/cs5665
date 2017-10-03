import sys, re

mobile_access = 'mobile_access.log'
desktop_access = 'desktop_access.log'


mobile_file = open(mobile_access,"w")
desktop_file = open(desktop_access,"w")

regex = 'mobile|Mobile'
pat = re.compile(regex)

with open("access.txt") as in_file:
    for line in in_file:
        if pat.search(line):
            mobile_file.write(line)
        else:
            desktop_file.write(line)
    mobile_file.close()
    desktop_file.close()
in_file.close()
