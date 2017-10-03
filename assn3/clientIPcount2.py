# ClientIPcount2.py
import sys, collections

# sys.argv is the list of command-line arguments
# sys.arg[0] is the name of the program itself
# sys.arg[1] is optional and will be the file name

# set input based on number of arguments
if len(sys.argv) == 1:
	f = sys.stdin
elif len(sys.argv) == 2:
	try:
		f = open(sys.argv[1])
	except IOError:
		print "Cannot open", sys.argv[1]
		sys.exit()
else:
	print "USAGE: python IPcount [FILE]"
	sys.exit()

addressCounts = collections.Counter()
# for every line passed into the script
for line in f:
	# find indices of client section
	start = line.find("[client ")
	if start >= 0 :
		end = line.find("]", start)
		# graph just the IP address
		address = line[start+8: end]
		addressCounts[address]=addressCounts[address]+1
		
#print top addresses
for address in addressCounts.most_common(20):
	sys.stdout.write(str(address) + "\n")