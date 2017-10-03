# matchregexgroup.py
import sys, re

# sys.argv is the list of command-line arguments
# sys.arg[0] is the name of the program itself
# sys.arg[1] will be the regex specified at the command line
# sys.arg[2] is optional and will be the file name

# set input and regular expression based on number of arguments
if len(sys.argv) == 2:
	regex = sys.argv[1]
	f = sys.stdin
elif len(sys.argv) == 3:
	regex = sys.argv[1]
	try:
		f = open(sys.argv[2])
	# catch exception, warn and exit if the file can't be opened
	except IOError:
		print "Cannot open", sys.argv[2]
		sys.exit()
# show USAGE message if wrong number of arguments
else:
	print "USAGE: python matchregexgroup PATTERN [FILE]"
	sys.exit()
	
# for every line passed into the script
for line in f:
	# if it matches the regex, write it to stdout
	m = re.search(regex, line)
	if m:
		sys.stdout.write(m.group(1) + "\n")