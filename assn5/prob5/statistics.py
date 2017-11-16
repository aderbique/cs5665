from matplotlib import pyplot as plt
from linear_algebra import sum_of_squares, dot
from collections import Counter
import math

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

def mean(sorted_values,len_sorted_values):
	return sum(sorted_values) / float(len_sorted_values)

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

def quantile(sorted_x,p,len_x):
    midpoint = p * (len_x-1)	
    if (midpoint == int(midpoint)):
        return sorted_x[int(midpoint)]
    else:
        lo = int(midpoint)
        hi = lo + 1
        return (hi - midpoint) * sorted_x[lo] + (midpoint - lo) * sorted_x[hi]
	
def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.iteritems()
            if count == max_count]		

def data_range(sorted_x):
    return sorted_x[-1] - sorted_x[0]

def de_mean(x,len_x):
    x_bar = mean(x,len_x)
    return [x_i - x_bar for x_i in x]	

def variance(x, len_x):
    deviations = de_mean(x,len_x)
    return sum_of_squares(deviations) / len_x	

def standard_deviation(x, len_x):
    return math.sqrt(variance(x,len(x))*(float(len_x)/float(len_x-1)))

def interquartile_range(x,len_x):
    return quantile(x, 0.75,len_x) - quantile(x, 0.25,len_x)

def normalize(x,len_x):
    x_bar = mean(x,len_x)
    sigma = standard_deviation(x,len_x)
    return [(x_i - x_bar)/sigma for x_i in x]

def covariance(x, y,len_x):
    return dot(de_mean(x,len_x), de_mean(y,len(y))) / (len_x - 1)
	
def covariance(x, y,len_x):
    return dot(de_mean(x,len_x), de_mean(y,len(y))) / len_x
	
def correlation(x, y):
    stdev_x = standard_deviation(x,len(y))
    stdev_y = standard_deviation(y,len(y))
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y,len_x) / stdev_x / stdev_y
    else:
        return 0 # if no variation, correlation is zero	

