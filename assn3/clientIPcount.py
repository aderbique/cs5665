# ClientIPcount.py
import sys

# sys.argv is the list of command-line arguments
# sys.arg[0] is the name of the program itself
# sys.arg[1] is optional and will be the file name

# set input based on number of arguments
if len(sys.argv) == 1:
	f = sys.stdin
elif len(sys.argv) == 2:
	try:
		f = open(sys.argv[1])
	# catch exception, warn and exit if the file can't be opened
	except IOError:
		print "Cannot open", sys.argv[1]
		sys.exit()
# show USAGE message if wrong number of arguments
else:
	print "USAGE: python IPcount [FILE]"
	sys.exit()

addressCounts = {}
# for every line passed into the script
for line in f:
	# find indices of client section
	start = line.find("[client ")
	if start >= 0 :
		end = line.find("]", start)
		# graph just the IP address
		address = line[start+8: end]
		if address in addressCounts:
			addressCounts[address] = addressCounts[address] + 1
		else:
			addressCounts[address] = 1
		
for address in addressCounts:
	sys.stdout.write(address + "," + str(addressCounts[address]) + "\n")