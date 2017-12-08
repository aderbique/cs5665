from __future__ import division
from collections import Counter
from functools import partial
from linear_algebra import dot, vector_add
#from gradient_descent import maximize_stochastic, maximize_batch
from working_with_data import rescale
from machine_learning import train_test_split
from multiple_regression import estimate_beta, predict, multiple_r_squared
import math, random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


x = [[1,49,4,0],[1,41,9,0],[1,40,8,0],[1,25,6,0],[1,21,1,0],[1,21,0,0],[1,19,3,0],[1,19,0,0],[1,18,9,0],[1,18,8,0],[1,16,4,0],[1,15,3,0],[1,15,0,0],[1,15,2,0],[1,15,7,0],[1,14,0,0],[1,14,1,0],[1,13,1,0],[1,13,7,0],[1,13,4,0],[1,13,2,0],[1,12,5,0],[1,12,0,0],[1,11,9,0],[1,10,9,0],[1,10,1,0],[1,10,1,0],[1,10,7,0],[1,10,9,0],[1,10,1,0],[1,10,6,0],[1,10,6,0],[1,10,8,0],[1,10,10,0],[1,10,6,0],[1,10,0,0],[1,10,5,0],[1,10,3,0],[1,10,4,0],[1,9,9,0],[1,9,9,0],[1,9,0,0],[1,9,0,0],[1,9,6,0],[1,9,10,0],[1,9,8,0],[1,9,5,0],[1,9,2,0],[1,9,9,0],[1,9,10,0],[1,9,7,0],[1,9,2,0],[1,9,0,0],[1,9,4,0],[1,9,6,0],[1,9,4,0],[1,9,7,0],[1,8,3,0],[1,8,2,0],[1,8,4,0],[1,8,9,0],[1,8,2,0],[1,8,3,0],[1,8,5,0],[1,8,8,0],[1,8,0,0],[1,8,9,0],[1,8,10,0],[1,8,5,0],[1,8,5,0],[1,7,5,0],[1,7,5,0],[1,7,0,0],[1,7,2,0],[1,7,8,0],[1,7,10,0],[1,7,5,0],[1,7,3,0],[1,7,3,0],[1,7,6,0],[1,7,7,0],[1,7,7,0],[1,7,9,0],[1,7,3,0],[1,7,8,0],[1,6,4,0],[1,6,6,0],[1,6,4,0],[1,6,9,0],[1,6,0,0],[1,6,1,0],[1,6,4,0],[1,6,1,0],[1,6,0,0],[1,6,7,0],[1,6,0,0],[1,6,8,0],[1,6,4,0],[1,6,2,1],[1,6,1,1],[1,6,3,1],[1,6,6,1],[1,6,4,1],[1,6,4,1],[1,6,1,1],[1,6,3,1],[1,6,4,1],[1,5,1,1],[1,5,9,1],[1,5,4,1],[1,5,6,1],[1,5,4,1],[1,5,4,1],[1,5,10,1],[1,5,5,1],[1,5,2,1],[1,5,4,1],[1,5,4,1],[1,5,9,1],[1,5,3,1],[1,5,10,1],[1,5,2,1],[1,5,2,1],[1,5,9,1],[1,4,8,1],[1,4,6,1],[1,4,0,1],[1,4,10,1],[1,4,5,1],[1,4,10,1],[1,4,9,1],[1,4,1,1],[1,4,4,1],[1,4,4,1],[1,4,0,1],[1,4,3,1],[1,4,1,1],[1,4,3,1],[1,4,2,1],[1,4,4,1],[1,4,4,1],[1,4,8,1],[1,4,2,1],[1,4,4,1],[1,3,2,1],[1,3,6,1],[1,3,4,1],[1,3,7,1],[1,3,4,1],[1,3,1,1],[1,3,10,1],[1,3,3,1],[1,3,4,1],[1,3,7,1],[1,3,5,1],[1,3,6,1],[1,3,1,1],[1,3,6,1],[1,3,10,1],[1,3,2,1],[1,3,4,1],[1,3,2,1],[1,3,1,1],[1,3,5,1],[1,2,4,1],[1,2,2,1],[1,2,8,1],[1,2,3,1],[1,2,1,1],[1,2,9,1],[1,2,10,1],[1,2,9,1],[1,2,4,1],[1,2,5,1],[1,2,0,1],[1,2,9,1],[1,2,9,1],[1,2,0,1],[1,2,1,1],[1,2,1,1],[1,2,4,1],[1,1,0,1],[1,1,2,1],[1,1,2,1],[1,1,5,1],[1,1,3,1],[1,1,10,1],[1,1,6,1],[1,1,0,1],[1,1,8,1],[1,1,6,1],[1,1,4,1],[1,1,9,1],[1,1,9,1],[1,1,4,1],[1,1,2,1],[1,1,9,1],[1,1,0,1],[1,1,8,1],[1,1,6,1],[1,1,1,1],[1,1,1,1],[1,1,5,1]]
daily_minutes_good = [68.77,51.25,52.08,38.36,44.54,57.13,51.4,41.42,31.22,34.76,54.01,38.79,47.59,49.1,27.66,41.03,36.73,48.65,28.12,46.62,35.57,32.98,35,26.07,23.77,39.73,40.57,31.65,31.21,36.32,20.45,21.93,26.02,27.34,23.49,46.94,30.5,33.8,24.23,21.4,27.94,32.24,40.57,25.07,19.42,22.39,18.42,46.96,23.72,26.41,26.97,36.76,40.32,35.02,29.47,30.2,31,38.11,38.18,36.31,21.03,30.86,36.07,28.66,29.08,37.28,15.28,24.17,22.31,30.17,25.53,19.85,35.37,44.6,17.23,13.47,26.33,35.02,32.09,24.81,19.33,28.77,24.26,31.98,25.73,24.86,16.28,34.51,15.23,39.72,40.8,26.06,35.76,34.76,16.13,44.04,18.03,19.65,32.62,35.59,39.43,14.18,35.24,40.13,41.82,35.45,36.07,43.67,24.61,20.9,21.9,18.79,27.61,27.21,26.61,29.77,20.59,27.53,13.82,33.2,25,33.1,36.65,18.63,14.87,22.2,36.81,25.53,24.62,26.25,18.21,28.08,19.42,29.79,32.8,35.99,28.32,27.79,35.88,29.06,36.28,14.1,36.63,37.49,26.9,18.58,38.48,24.48,18.95,33.55,14.24,29.04,32.51,25.63,22.22,19,32.73,15.16,13.9,27.2,32.01,29.27,33,13.74,20.42,27.32,18.23,35.35,28.48,9.08,24.62,20.12,35.26,19.92,31.02,16.49,12.16,30.7,31.22,34.65,13.13,27.51,33.2,31.57,14.1,33.42,17.44,10.12,24.42,9.82,23.39,30.93,15.03,21.67,31.09,33.29,22.61,26.89,23.48,8.38,27.81,32.35,23.84]

# Extract the individual lists.
constant, num_friends, work_hours_per_day, noPhD = zip(*x)

num_friends_list = [[1,x] for x in num_friends]
work_hours_per_day_list = [[1,x] for x in work_hours_per_day]
daily_minutes_good_list = [[1,x] for x in daily_minutes_good]


###########################################################################################
# Let's look at the case of trying to predict a binary outcome using our least squares lines.
# Recall that it was ok to use data that consisted of whole numbers as input to our
# prior regression models.
# What if we try to model such data as output?
#
# We will try to predict whether or not an individual has a PhD based on other information.
###########################################################################################

# This relationship doesn't show much promise.
plt.scatter(work_hours_per_day,noPhD)
plt.title("noPhD by work_hours_per_day")
plt.xlabel("work_hours_per_day")
plt.ylabel("noPhD")
plt.show()  

# The r-squared is about as low as it can be.
random.seed(0)
xtest = work_hours_per_day_list
beta = estimate_beta(xtest, noPhD) 
print "\nbeta=", beta, "\nr-squared=", multiple_r_squared(xtest, noPhD, beta), "\n\n"

# The regression line is almost flat.
plt.scatter(work_hours_per_day,noPhD)
plt.title("noPhD by work_hours_per_day")
plt.xlabel("work_hours_per_day")
plt.ylabel("noPhD")
plt.plot([min(work_hours_per_day),max(work_hours_per_day)],[predict([1,min(work_hours_per_day)],beta),predict([1,max(work_hours_per_day)],beta)])
plt.show()  

###########################################################################################

# This one is a bit more promising, but there is alot of overlap.
plt.scatter(daily_minutes_good,noPhD)
plt.title("noPhD by daily_minutes_good")
plt.xlabel("daily_minutes_good")
plt.ylabel("noPhD")
plt.show() 

# Once again, a small r-squared.
random.seed(0)
xtest = daily_minutes_good_list
beta = estimate_beta(xtest, noPhD) 
print "\nbeta=", beta, "\nr-squared=", multiple_r_squared(xtest, noPhD, beta), "\n\n"

# Plot the line and get some idea of how this might work.
# It is a stretch, but you might think of the linear predictions as probabilities.
plt.scatter(daily_minutes_good,noPhD)
plt.title("noPhD by daily_minutes_good")
plt.xlabel("daily_minutes_good")
plt.ylabel("noPhD")
plt.plot([min(daily_minutes_good),max(daily_minutes_good)],[predict([1,min(daily_minutes_good)],beta),predict([1,max(daily_minutes_good)],beta)])
plt.show()  

# Here is how the linear predictions compare to the noPhD values.
# Note several things:
# There is a negative value. This wouldn't be allowed for a probability.
# There is a lot of overlap.
# Perhaps a cut-off of 0.5 would work, but there would be lots of errors.
predfromline=[predict([1,d],beta) for d in daily_minutes_good]
plt.scatter(predfromline,noPhD)
plt.title("noPhD by linear prediction using daily_minutes_good")
plt.xlabel("linear prediction")
plt.ylabel("noPhD")
plt.show()  


###########################################################################################
# Based on num_friends, it appears that we can predict noPhD quite well.
# Intuitively we might do this using a simple threshold, which is similar to what would
# be done in a decision tree.
plt.scatter(num_friends,noPhD)
plt.title("noPhD by num_friends")
plt.xlabel("num_friends")
plt.ylabel("noPhD")
plt.show() 

# We will continue down the path of using our linear regression models to predict the binary values.
# With that said, the r-squared value is great for the linear mapping. We will return to that later.
random.seed(0)
xtest = num_friends_list
beta = estimate_beta(xtest, noPhD) 
print "\nbeta=", beta, "\nr-squared=", multiple_r_squared(xtest, noPhD, beta), "\n\n"

# If we selected the right cutoff value (not 0.5), we could get a near perfect prediction.
plt.scatter(num_friends,noPhD)
plt.title("noPhD by num_friends")
plt.xlabel("num_friends")
plt.ylabel("noPhD")
plt.plot([min(num_friends),max(num_friends)],[predict([1,min(num_friends)],beta),predict([1,max(num_friends)],beta)])
plt.show()  
###########################################################################################

# A line wasn't a good fit, even in the best case above. 
# And the whole idea of using a linear function for this purpose may seem silly at this point.
# But, there is a function that can help us - the logistic function.
#
# NOTE: Logistic Regression is covered in Chapter 16 - Logistic Regression.
#
# What values can the following function have? What does it look like?
# It falls between 0 and 1.
def logistic(x):
    return 1.0 / (1 + math.exp(-x))

xs = [xi/10.0 for xi in range(-100,100)]
ys = [logistic(xi) for xi in xs]

# Does the plot look helpful for our prior situation?
plt.plot(xs,ys)
plt.title("The Logistic Function")
plt.xlabel("x")
plt.ylabel("logistic(x)")
plt.show() 

# Use the logistic function to get a better approximation.
xs = [xi/10.0 for xi in range(0,500)]
ys = [1-logistic((xi-6.0)) for xi in xs]
plt.scatter(num_friends,noPhD,color='blue')
plt.plot(xs,ys,color='red')
plt.title("noPhD by num_friends")
plt.xlabel("num_friends")
plt.ylabel("noPhD")
plt.show() 

# Use the logistic function to get an even better approximation.
# Close but not quite.
xs = [xi/10.0 for xi in range(0,500)]
ys = [1-logistic(10.0*(xi-6.0)) for xi in xs]
plt.scatter(num_friends,noPhD,color='blue')
plt.plot(xs,ys,color='red')
plt.title("noPhD by num_friends")
plt.xlabel("num_friends")
plt.ylabel("noPhD")
plt.show() 

# Use the logistic function to get an even better approximation.
# Very close.
# Note that the expression within the call to the logistic function is linear.
xs = [xi/10.0 for xi in range(0,500)]
ys = [1-logistic(100.0*(xi-6.0)) for xi in xs]
plt.scatter(num_friends,noPhD,color='blue')
plt.plot(xs,ys,color='red')
plt.title("noPhD by num_friends")
plt.xlabel("num_friends")
plt.ylabel("noPhD")
plt.show() 

# This is the derivative of the logistic function.
def logistic_prime(x):
    return logistic(x) * (1 - logistic(x))

# Rather than choose beta to minimize the sum of squares, 
# we choose beta to maximize the likelihood of the data.
# Find the linear expression that when composed within the
# logistic function produces the highest probability of the data.
# This is equivalent to maximizing the log of the likelihood,
# called the log-likelihood, because the logarithm is a 
# strictly-increasing function.
# See the formula in our book, page 103. Note the simplification
# that comes when y_i=0 or y_i=1.
def logistic_log_likelihood_i(x_i, y_i, beta):
    if y_i == 1:
        return math.log(logistic(dot(x_i, beta)))
    else:
        return math.log(1 - logistic(dot(x_i, beta)))

# This is the likelihood over the set of data.
def logistic_log_likelihood(x, y, beta):
    return sum(logistic_log_likelihood_i(x_i, y_i, beta)
               for x_i, y_i in zip(x, y))

# The partial derivative. i is the index of the data point,
# j is the index of the derivative.
def logistic_log_partial_ij(x_i, y_i, beta, j):
    return (y_i - logistic(dot(x_i, beta))) * x_i[j]

# The gradient consists of the partials.
# Note that the enumerate function creates an iterator
# that pairs the element with the index of the element.
# This is the gradient relative to a single data point.
def logistic_log_gradient_i(x_i, y_i, beta):
    return [logistic_log_partial_ij(x_i, y_i, beta, j)
            for j, _ in enumerate(beta)]

# This is the gradient over all of the data points.
def logistic_log_gradient(x, y, beta):
    return reduce(vector_add,
                  [logistic_log_gradient_i(x_i, y_i, beta)
                   for x_i, y_i in zip(x,y)])    

# Uncharacteristically, our author stops short of creating functions to tie this altogether.
# We'll go ahead and create them here.

# Compute beta via batch gradient descent (ascent) maximization.
def logistic_batch(x,y,beta_0):
    fn = partial(logistic_log_likelihood, x, y)
    gradient_fn = partial(logistic_log_gradient, x, y)
    beta_hat = maximize_batch(fn, gradient_fn, beta_0)
    return beta_hat
	
# Compute beta via stochastic gradient descent (ascent) maximization.
def logistic_stochastic(x,y,beta_0):
    beta_hat = maximize_stochastic(logistic_log_likelihood_i, logistic_log_gradient_i, x, y, beta_0)
    return beta_hat

# We can run this in a manner similar to what was done for linear regression.
x = [[1,n] for n in num_friends]
y = noPhD
beta_0 = [1,1]

# Unfortunately, this takes awhile to run.
#logistic_batch(x,y,beta_0)

# So, here is the result:
beta_hat = [37.761750837700475, -6.35447800446096]

# Here is the corresponding predict function to use the model.
def predict_logistic(x_i,beta):
    return logistic(dot(x_i,beta))

# Plug in some values. 
# The following give results very near 1.
predict_logistic([1,1],beta_hat)
predict_logistic([1,2],beta_hat)
predict_logistic([1,3],beta_hat)
predict_logistic([1,4],beta_hat)
predict_logistic([1,5],beta_hat)

# This falls in between, which makes sense.
# Values near are also in between.
# Remember that our inputs were whole numbers.
predict_logistic([1,6],beta_hat)
predict_logistic([1,6.1],beta_hat)
predict_logistic([1,5.9],beta_hat)

# The following is very close to zero, as it should be.
predict_logistic([1,7],beta_hat)

# Plot it. Note that this is close to what we guessed at earlier.
xs = [xi/10.0 for xi in range(0,500)]
ys = [predict_logistic([1,xi],beta_hat) for xi in xs]
plt.scatter(num_friends,noPhD,color='blue')
plt.plot(xs,ys,color='red')
plt.title("noPhD by num_friends")
plt.xlabel("num_friends")
plt.ylabel("noPhD")
plt.show() 

###########################################################################################
# How should we evaluate our results for logistic regression?
# How did we previously evaluate our results? Sum-of-squared errors!
# Does that work here?
# We probably need something else since our data is binary.
# And, we probably should separate training and testing.
#
# NOTE: Some of the following comes from Chapter 11 - Machine Learning.
###########################################################################################

# This function splits data into two sets proportioned as [prob, 1-prob].
def split_data(data, prob):
    results = [], []
    for row in data:
        results[0 if random.random() < prob else 1].append(row)
    return results

# This function splits training and testing x and y sets.
# Note that the pct give is the percentage allocated to testing.
def train_test_split(x, y, test_pct):
    data = zip(x, y)                              # pair corresponding values  
    train, test = split_data(data, 1 - test_pct)  # split the dataset of pairs
    x_train, y_train = zip(*train)                # magical un-zip trick
    x_test, y_test = zip(*test)
    return x_train, x_test, y_train, y_test

# Split data for training and testing.
# We are going to use smaller training sets to help us computationally.
# Sizes and amounts may vary depending on the application and testing intentions.
random.seed(0)
x_train, x_test, y_train, y_test = train_test_split(x, y, 0.75)

# Form the logistic regression model for the training data.
# The following takes about 10 seconds.
beta_0 = [1,1]
beta_hat = logistic_batch(x_train,y_train,beta_0)

# Beta won't be exactly what we computed for the full model. It is close though.
beta_hat

# For the purposes of evaluation, we will focus on comparison of the binary predictions
# with the binary data. For the following, we assume 1 represents a "positive" outcome,
# and 0 represents a "negative" outcome. In this case, we can characterize the result of
# a single prediction relative to positive and negative, and we get four possibilities:
# true positive, false negative, false positive and true negative.
# The following function counts these over a data set, presumably a "test" data set.
def classification_performance_summary(x_test, y_test, beta):
    true_positives = 0
    false_positives = 0
    true_negatives = 0
    false_negatives = 0
    for x_i, y_i in zip(x_test, y_test):
        predict = round(logistic(dot(beta_hat, x_i)))
        if y_i == 1 and predict == 1: 
            true_positives += 1
        elif y_i == 1 and predict == 0:
            false_negatives += 1
        elif y_i == 0 and predict == 1:
            false_positives += 1
        else:
            true_negatives += 1
    return true_positives, false_positives, true_negatives, false_negatives

# This yields counts for: true positives, false positives, true negatives, false negatives.
tp, fp, tn, fn = classification_performance_summary(x_test,y_test,beta_hat)

# Print them out.
tp, fp, tn, fn

# The raw counts are helpful, but comparison is limited to instance where we have the
# same amount of test data.
# There are a number of ways these values can be combined to give measures of performance
# that can be compared regardless of size of test and training sets, etc.

# Accuracy is the ratio of overall correctly-classified items.
def accuracy(tp, fp, fn, tn):
    correct = tp + tn
    total = tp + fp + fn + tn
    return correct / total

# Precision is the ratio of true positives to all identified as positive.
def precision(tp, fp, fn, tn):
    return tp / (tp + fp)

# Recall is the ratio of true positives to all that should have been identified as positive.
def recall(tp, fp, fn, tn):
    return tp / (tp + fn)

# the F1 score is the harmonic mean of precision and recall.
def f1_score(tp, fp, fn, tn):
    p = precision(tp, fp, fn, tn)
    r = recall(tp, fp, fn, tn)
    return 2 * p * r / (p + r)

# All of these are high for the current run.
print "\n\n\n", "Accuracy = " , round(accuracy(tp, fp, fn, tn),3) , "Precision = " , round(precision(tp, fp, fn, tn),3) , \
    "Recall = " , round(recall(tp, fp, fn, tn),3) , "F1 = " , round(f1_score(tp, fp, fn, tn),3) , "\n\n\n"

# Do 5 runs and compare results.
for i in range(5):
    x_train, x_test, y_train, y_test = train_test_split(x, y, 0.75)
    beta_hat = logistic_batch(x_train,y_train,beta_0)
    tp, fp, tn, fn = classification_performance_summary(x_test,y_test,beta_hat)
    print "Accuracy = " , round(accuracy(tp, fp, fn, tn),3) , "Precision = " , round(precision(tp, fp, fn, tn),3) , \
    	"Recall = " , round(recall(tp, fp, fn, tn),3) , "F1 = " , round(f1_score(tp, fp, fn, tn),3)

# Do 5 more runs with reduced train pct.
for i in range(5):
    x_train, x_test, y_train, y_test = train_test_split(x, y, 0.9)
    beta_hat = logistic_batch(x_train,y_train,beta_0)
    tp, fp, tn, fn = classification_performance_summary(x_test,y_test,beta_hat)
    print "Accuracy = " , round(accuracy(tp, fp, fn, tn),3) , "Precision = " , round(precision(tp, fp, fn, tn),3) , \
    	"Recall = " , round(recall(tp, fp, fn, tn),3) , "F1 = " , round(f1_score(tp, fp, fn, tn),3)

# Expand the model. Is it better? Run multiple times and do a statistical significance test.
# Each run takes about 30 seconds, so we will run it once.
x = [[1,num_friends[n],work_hours_per_day[n],daily_minutes_good[n]] for n in range(len(num_friends))]
y = noPhD
beta_0 = [1,1,1,1]
x_train, x_test, y_train, y_test = train_test_split(x, y, 0.9)
beta_hat = logistic_batch(x_train,y_train,beta_0)
tp, fp, tn, fn = classification_performance_summary(x_test,y_test,beta_hat)
print "Accuracy = " , round(accuracy(tp, fp, fn, tn),3) , "Precision = " , round(precision(tp, fp, fn, tn),3) , \
	"Recall = " , round(recall(tp, fp, fn, tn),3) , "F1 = " , round(f1_score(tp, fp, fn, tn),3)


###########################################################################################
# Our author uses the following example.
# Model whether users have premium (paid) accounts based on experience and salary.
###########################################################################################

# Data is of the form (experience, salary, premium account)
data = [(0.7,48000,1),(1.9,48000,0),(2.5,60000,1),(4.2,63000,0),(6,76000,0),(6.5,69000,0),(7.5,76000,0),(8.1,88000,0),(8.7,83000,1),(10,83000,1),(0.8,43000,0),(1.8,60000,0),(10,79000,1),(6.1,76000,0),(1.4,50000,0),(9.1,92000,0),(5.8,75000,0),(5.2,69000,0),(1,56000,0),(6,67000,0),(4.9,74000,0),(6.4,63000,1),(6.2,82000,0),(3.3,58000,0),(9.3,90000,1),(5.5,57000,1),(9.1,102000,0),(2.4,54000,0),(8.2,65000,1),(5.3,82000,0),(9.8,107000,0),(1.8,64000,0),(0.6,46000,1),(0.8,48000,0),(8.6,84000,1),(0.6,45000,0),(0.5,30000,1),(7.3,89000,0),(2.5,48000,1),(5.6,76000,0),(7.4,77000,0),(2.7,56000,0),(0.7,48000,0),(1.2,42000,0),(0.2,32000,1),(4.7,56000,1),(2.8,44000,1),(7.6,78000,0),(1.1,63000,0),(8,79000,1),(2.7,56000,0),(6,52000,1),(4.6,56000,0),(2.5,51000,0),(5.7,71000,0),(2.9,65000,0),(1.1,33000,1),(3,62000,0),(4,71000,0),(2.4,61000,0),(7.5,75000,0),(9.7,81000,1),(3.2,62000,0),(7.9,88000,0),(4.7,44000,1),(2.5,55000,0),(1.6,41000,0),(6.7,64000,1),(6.9,66000,1),(7.9,78000,1),(8.1,102000,0),(5.3,48000,1),(8.5,66000,1),(0.2,56000,0),(6,69000,0),(7.5,77000,0),(8,86000,0),(4.4,68000,0),(4.9,75000,0),(1.5,60000,0),(2.2,50000,0),(3.4,49000,1),(4.2,70000,0),(7.7,98000,0),(8.2,85000,0),(5.4,88000,0),(0.1,46000,0),(1.5,37000,0),(6.3,86000,0),(3.7,57000,0),(8.4,85000,0),(2,42000,0),(5.8,69000,1),(2.7,64000,0),(3.1,63000,0),(1.9,48000,0),(10,72000,1),(0.2,45000,0),(8.6,95000,0),(1.5,64000,0),(9.8,95000,0),(5.3,65000,0),(7.5,80000,0),(9.9,91000,0),(9.7,50000,1),(2.8,68000,0),(3.6,58000,0),(3.9,74000,0),(4.4,76000,0),(2.5,49000,0),(7.2,81000,0),(5.2,60000,1),(2.4,62000,0),(8.9,94000,0),(2.4,63000,0),(6.8,69000,1),(6.5,77000,0),(7,86000,0),(9.4,94000,0),(7.8,72000,1),(0.2,53000,0),(10,97000,0),(5.5,65000,0),(7.7,71000,1),(8.1,66000,1),(9.8,91000,0),(8,84000,0),(2.7,55000,0),(2.8,62000,0),(9.4,79000,0),(2.5,57000,0),(7.4,70000,1),(2.1,47000,0),(5.3,62000,1),(6.3,79000,0),(6.8,58000,1),(5.7,80000,0),(2.2,61000,0),(4.8,62000,0),(3.7,64000,0),(4.1,85000,0),(2.3,51000,0),(3.5,58000,0),(0.9,43000,0),(0.9,54000,0),(4.5,74000,0),(6.5,55000,1),(4.1,41000,1),(7.1,73000,0),(1.1,66000,0),(9.1,81000,1),(8,69000,1),(7.3,72000,1),(3.3,50000,0),(3.9,58000,0),(2.6,49000,0),(1.6,78000,0),(0.7,56000,0),(2.1,36000,1),(7.5,90000,0),(4.8,59000,1),(8.9,95000,0),(6.2,72000,0),(6.3,63000,0),(9.1,100000,0),(7.3,61000,1),(5.6,74000,0),(0.5,66000,0),(1.1,59000,0),(5.1,61000,0),(6.2,70000,0),(6.6,56000,1),(6.3,76000,0),(6.5,78000,0),(5.1,59000,0),(9.5,74000,1),(4.5,64000,0),(2,54000,0),(1,52000,0),(4,69000,0),(6.5,76000,0),(3,60000,0),(4.5,63000,0),(7.8,70000,0),(3.9,60000,1),(0.8,51000,0),(4.2,78000,0),(1.1,54000,0),(6.2,60000,0),(2.9,59000,0),(2.1,52000,0),(8.2,87000,0),(4.8,73000,0),(2.2,42000,1),(9.1,98000,0),(6.5,84000,0),(6.9,73000,0),(5.1,72000,0),(9.1,69000,1),(9.8,79000,1),]
data = map(list, data) # change tuples to lists

# Use experience and salary to predict whether a user has a paid account.
x = [[1] + row[:2] for row in data] # each element is [1, experience, salary]
y = [row[2] for row in data]        # each element is paid_account

# Extract these separately so they can be plotted, etc.
experience = [d[0] for d in data]
salary = [d[1] for d in data]
paid = [d[2] for d in data]

# Separate data by paid and unpaid.
paid_indexes = [i for i in range(len(paid)) if paid[i] == 1]
unpaid_indexes = [i for i in range(len(paid)) if paid[i] == 0]

paid_experience = [experience[i] for i in paid_indexes]
unpaid_experience = [experience[i] for i in unpaid_indexes]
paid_salary = [salary[i] for i in paid_indexes]
unpaid_salary = [salary[i] for i in unpaid_indexes]

# Plot it it. Notice the apparent separation of the data.
plt.scatter(paid_experience,paid_salary, marker='x', color='black')
plt.scatter(unpaid_experience,unpaid_salary, marker='o', color='grey')
plt.title("Paid and Unpaid Users")
plt.xlabel("experience")
plt.ylabel("salary")
plt.show()

# Rescale the data to avoid problems with values.
rescale_x = rescale(x)
beta_0 = [1,1,1]
beta_hat = logistic_batch(rescale_x,y,beta_0)

beta_hat

# The result should be approximately [-2.11, 4.54, -4.41].
# This translates to paid = logistic(-2.11 + 4.54 * experience_rescaled - 4.41 * salary_rescaled).
# Take the linear expression, set equal to zero, translate it back to unscaled units, and we get roughly:
# salary = 5615.11 * experience + 31167.71

# Plot this equation along with our original data.
# How well does it separate the two types of data?
# How does the logistic function come into play?
# NOTE: The is not the least squares line for the original data.
# It is the linear expression found to maximize likelihood of the logistic function relative to the data.
plt.plot([0,10],[31167.71, 5615.11 * 10 + 31167.71])
plt.scatter(paid_experience,paid_salary, marker='x', color='black')
plt.scatter(unpaid_experience,unpaid_salary, marker='o', color='grey')
plt.title("Paid and Unpaid Users")
plt.xlabel("experience")
plt.ylabel("salary")
plt.show()

# Is this data linearly separable?

# What other approaches try to "separate" data? Support Vector Machines

# What if the data is not linearly-separable?
