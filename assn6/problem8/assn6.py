from linear_algebra import sum_of_squares, dot
from collections import Counter
import math

def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

def sort_list(num_friends):
	return sorted(num_friends)

def mean(sorted_values,len_sorted_values):
	return sum(sorted_values) / float(len_sorted_values)
  
def variance(x, len_x):
    deviations = de_mean(x,len_x)
    return sum_of_squares(deviations) / len_x	  
  
def standard_deviation(x, len_x):
    return math.sqrt(variance(x,len(x))*(float(len_x)/float(len_x-1)))
  
def normalize(x,len_x):
    x_bar = mean(x,len_x)
    sigma = standard_deviation(x,len_x)
    return [(x_i - x_bar)/sigma for x_i in x]
  


a = np.arange(20)
moving_average(a)
moving_average(a,n=4)

