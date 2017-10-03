#!/user/bin/python3

#Austin Derbique
#A01967241
#9/12/17
#CS5460 Data Science: Assignment 3

import sys, re

# sys.argv is the list of command-line arguments
# sys.arg[0] is the name of the program itself
# sys.arg[1] will be the regex specified at the command line
# sys.arg[2] is optional and will be the file name

# set input and regular expression based on number of arguments
if len(sys.argv) == 2:
	N = sys.argv[1]
	filename = sys.stdin
elif len(sys.argv) == 3:
	N = sys.argv[1]
	try:
		filename = sys.argv[2]
	# catch exception, warn and exit if the file can't be opened
	except IOError:
		print("Cannot open", sys.argv[2])
		sys.exit()
# show USAGE message if wrong number of arguments
else:
	print("USAGE: python ehead.py N [FILENAME]")
	sys.exit()
	
# for every line passed into the script

with open(filename) as myfile:
	firstNlines = myfile.readlines()[0:int(N)]
