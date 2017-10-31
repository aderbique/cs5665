from __future__ import division
from collections import Counter
import math, random
from matplotlib import pyplot as plt


#################################################################################################################################
## The birthday problem
#
## Simulate a birthdate.
#random.randint(1,365)
#
## Simulate 40 birthdates.
#[random.randint(1,365) for _ in range(40)]
#
## Count to see if there are any the same - we get a dictionary back.
#Counter([random.randint(1,365) for _ in range(40)])
#
## Get the most common outcome.
#Counter([random.randint(1,365) for _ in range(40)]).most_common(1)
#
## This returns a list.
#Counter([random.randint(1,365) for _ in range(40)]).most_common()
#
## Extract the counts - the dates don't really matter.
#[y for x,y in Counter([random.randint(1,365) for _ in range(40)]).most_common()]
#
## Repeat 10 times.
#[[y for x,y in Counter([random.randint(1,365) for _ in range(40)]).most_common()] for _ in range(1000)]
#
## Try to tabulate the results. But there is a problem with this ...
#Counter([[y for x,y in Counter([random.randint(1,365) for _ in range(40)]).most_common()] for _ in range(1000)])
#
## Cast as strings and it will work.
#Counter([str([y for x,y in Counter([random.randint(1,365) for _ in range(40)]).most_common()]) for _ in range(1000)])
#
## Get it as a list.
#Counter([str([y for x,y in Counter([random.randint(1,365) for _ in range(40)]).most_common()]) for _ in range(1000)]).most_common()
#
## This representation is a bit more concise.
#Counter([str(Counter([y for x,y in Counter([random.randint(1,365) for _ in range(40)]).most_common()]).most_common()) for _ in range(1000)]).most_common()
#
## Now let's show a bar chart for this ...
#commonbirthdaycounts = Counter([str(Counter([y for x,y in Counter([random.randint(1,365) for _ in range(40)]).most_common()]).most_common()) for _ in range(1000)]).most_common()
## * is the "unpack" or splat operator. It unpacks a list and turns the elements into arguments. In turn, we can extract the individual lists.
#labels, counts = zip(*commonbirthdaycounts)
#indexes = [i+0.1 for i,_ in enumerate(labels)]
## Now plot it. But ... this is a bit cluttered.
#plt.bar(indexes, counts)
#plt.title("Common Birthday Counts")
#plt.xlabel("distribution")
#plt.ylabel("count")
#plt.xticks([i + 0.1 for i, _ in enumerate(labels)],labels)
#plt.show()
#
## To get rid of some of the clutter, flip the chart to be a horizontal bar chart.
#labels, counts = zip(*commonbirthdaycounts)
#indexes = [i+0.1 for i,_ in enumerate(labels)]
#plt.barh(indexes, counts)
#plt.title("Common Birthday Counts")
#plt.ylabel("distribution")
#plt.xlabel("count")
#plt.yticks([i + 0.1 for i, _ in enumerate(labels)],labels)
#plt.show()

# Turn it into a function so we can run it repeatedly
def birthday_simulation(numpeople,numsimulations):
    commonbirthdaycounts = Counter([str(Counter([y for x,y in Counter([random.randint(1,365) for _ in range(numpeople)]).most_common()]).most_common()) for _ in range(numsimulations)]).most_common()
    labels, counts = zip(*commonbirthdaycounts)
    indexes = [i+0.1 for i,_ in enumerate(labels)]
    plt.barh(indexes, counts)
    plt.title("Common Birthday Counts")
    plt.ylabel("distribution")
    plt.xlabel("count")
    plt.yticks([i + 0.1 for i, _ in enumerate(labels)],labels)
    plt.show()
    return
	
#birthday_simulation(40,1000)

# Examine lesser class sizes - where do we have a 50-50 chance of no two the same.
#birthday_simulation(37,1000)
#birthday_simulation(30,1000)
#birthday_simulation(20,1000)

# It looks like 50-50 happens near 23.
#birthday_simulation(23,1000)	

# We see more low-probability events with more runs.
#birthday_simulation(23,100000)	
#birthday_simulation(22,100000)	
#	
#########################################################################################################################################
## More coin tosses
## Now we look a "streaks", consecutive tosses the same.
#
##previoustoss = -1
##streak = 0
#maxstreak = 0
#for i in range(1000):
#    toss = random.randint(0,1)
#    if toss == previoustoss:
#        streak = streak + 1
#    else:
#        streak = 0
#    previoustoss = toss
#    if streak > maxstreak:
#        maxstreak = streak
#        print maxstreak
#
# Implement as a function.
def cointossstreak_simulation(numtrials):
    previoustoss = -1
    streak = 0
    maxstreak = 0
    for i in range(numtrials):
        toss = random.randint(0,1)
        if toss == previoustoss:
            streak = streak + 1
        else:
            streak = 0
        previoustoss = toss
        if streak > maxstreak:
            maxstreak = streak
    return(maxstreak)

# Try the following to see what we can compute in "reasonable" time.
#print cointossstreak_simulation(1000)
#print cointossstreak_simulation(10000)
#print cointossstreak_simulation(100000)
#print cointossstreak_simulation(1000000)
#print cointossstreak_simulation(10000000)

# Check memory on this one? What is the cause???
#print cointossstreak_simulation(100000000)
	
	
def cointossstreak_simulation(numtrials):
    previoustoss = -1
    streak = 0
    maxstreak = 0
    i = 0
    while i<numtrials:
        toss = random.randint(0,1)
        if toss == previoustoss:
            streak = streak + 1
        else:
            streak = 0
        previoustoss = toss
        if streak > maxstreak:
            maxstreak = streak
        i = i +1
    return(maxstreak)
	
# Check that the new version works.
#print cointossstreak_simulation(1000)
# Check memory. It should be better. Why?
#print cointossstreak_simulation(100000000)
#print cointossstreak_simulation(1000000000)
	