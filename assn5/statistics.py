from matplotlib import pyplot as plt
from collections import Counter

def make_friend_counts_histogram(plt):
    friend_counts = Counter(num_friends)
    xs = range(101)
    ys = [friend_counts[x] for x in xs]
    plt.bar(xs, ys)
    plt.axis([0,101,0,25])
    plt.title("Histogram of Friend Counts")
    plt.xlabel("# of friends")
    plt.ylabel("# of people")
    plt.show()

def sort_list(num_friends):
	return sorted(num_friends)


def min_max(sorted_values):
	return sorted_values[0],sorted_values[-1]


def mean(sorted_values):
	return sum(sorted_values) / float(len(sorted_values))


def median(sorted_v, len_v):
    midpoint = len_v // 2
    if len_v % 2 == 1:
        # if odd, return the middle value
        return sorted_v[midpoint]
    else:
        # if even, return the average of the middle values
        lo = midpoint - 1
        hi = midpoint
		# Note that in our book, the divisor is 2, not 2.0.
        return (sorted_v[lo] + sorted_v[hi]) / 2.0


# Consider this definition:
def quantile(sorted_x,p,len_x):
    midpoint = p * (len_x-1)	
    if (midpoint == int(midpoint)):
        return sorted_x[int(midpoint)]
    else:
        lo = int(midpoint)
        hi = lo + 1
        return (hi - midpoint) * sorted_x[lo] + (midpoint - lo) * sorted_x[hi]

# Is this correct? Think it over ...

# Next is the mode.		
def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.iteritems()
            if count == max_count]		

def data_range(sorted_x):
    return sorted_x[-1] - sorted_x[0]
	

def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]	

def variance(x, len_x):
    deviations = de_mean(x)
    return sum_of_squares(deviations) / len_x	
	
import math
from linear_algebra import sum_of_squares, dot


def standard_deviation(x, len_x):
    return math.sqrt(variance(x)*(float(len_x)/float(len_x-1)))
	
sample_standard_deviation(num_friends)

# Now define the interquartile range as another measure of dispersion.
def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)
	
interquartile_range(num_friends)	
	
# Not in our book - normalization by z-score.
# normalize
def normalize(x):
    x_bar = mean(x)
    sigma = standard_deviation(x)
    return [(x_i - x_bar)/sigma for x_i in x]

normalize(num_friends)	

######################################################################################################################

# Number of minutes spent on the DataScienster Website.
daily_minutes = [1,68.77,51.25,52.08,38.36,44.54,57.13,51.4,41.42,31.22,34.76,54.01,38.79,47.59,49.1,27.66,41.03,36.73,48.65,28.12,46.62,35.57,32.98,35,26.07,23.77,39.73,40.57,31.65,31.21,36.32,20.45,21.93,26.02,27.34,23.49,46.94,30.5,33.8,24.23,21.4,27.94,32.24,40.57,25.07,19.42,22.39,18.42,46.96,23.72,26.41,26.97,36.76,40.32,35.02,29.47,30.2,31,38.11,38.18,36.31,21.03,30.86,36.07,28.66,29.08,37.28,15.28,24.17,22.31,30.17,25.53,19.85,35.37,44.6,17.23,13.47,26.33,35.02,32.09,24.81,19.33,28.77,24.26,31.98,25.73,24.86,16.28,34.51,15.23,39.72,40.8,26.06,35.76,34.76,16.13,44.04,18.03,19.65,32.62,35.59,39.43,14.18,35.24,40.13,41.82,35.45,36.07,43.67,24.61,20.9,21.9,18.79,27.61,27.21,26.61,29.77,20.59,27.53,13.82,33.2,25,33.1,36.65,18.63,14.87,22.2,36.81,25.53,24.62,26.25,18.21,28.08,19.42,29.79,32.8,35.99,28.32,27.79,35.88,29.06,36.28,14.1,36.63,37.49,26.9,18.58,38.48,24.48,18.95,33.55,14.24,29.04,32.51,25.63,22.22,19,32.73,15.16,13.9,27.2,32.01,29.27,33,13.74,20.42,27.32,18.23,35.35,28.48,9.08,24.62,20.12,35.26,19.92,31.02,16.49,12.16,30.7,31.22,34.65,13.13,27.51,33.2,31.57,14.1,33.42,17.44,10.12,24.42,9.82,23.39,30.93,15.03,21.67,31.09,33.29,22.61,26.89,23.48,8.38,27.81,32.35,23.84]

from matplotlib import pyplot as plt

plt.scatter(num_friends,daily_minutes)
plt.title("# friends vs. minutes per day")
plt.xlabel("# of friends")
plt.ylabel("minutes per day")
plt.show()

# Our book's definition of covariance.
def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)
	
# Here is the correct definition.
def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / n
	
# Now define correlation:
def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0 # if no variation, correlation is zero	
		
# Now compute the correlation between number of friends and daily minutes.
correlation(num_friends,daily_minutes)		
	
# Reverse the order and what do we get?
correlation(daily_minutes,num_friends)		

# Our authors treatment of an apparent outlier:

outlier = num_friends.index(100) # index of outlier

num_friends_good = [x 
                    for i, x in enumerate(num_friends) 
                    if i != outlier]

daily_minutes_good = [x 
                      for i, x in enumerate(daily_minutes) 
                      if i != outlier]
					  
correlation(num_friends_good,daily_minutes_good)	

#####################################################################################################################################################
# Now look at boxplots ...

from matplotlib import pyplot as plt
plt.boxplot(num_friends)
plt.show()

