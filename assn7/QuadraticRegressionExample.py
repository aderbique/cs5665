########################################################################################################################
# This code is intended for one of the exercises in Assignment 7.
# It can be run stand-alone: python QuadraticRegressionExample.py
########################################################################################################################

from __future__ import division
import matplotlib.pyplot as plt
import numpy as np

def total_sum_of_squares(y):
    mean_y = sum(y)/float(len(y))
    return sum([(v-mean_y)**2 for v in y])

def multiple_regression(X,Y):
    tmp1 = np.matmul(X.T,X)
    tmp2 = np.linalg.inv(tmp1)
    tmp3 = np.matmul(tmp2,X.T)
    beta = np.matmul(tmp3,Y)
    return beta
	
def predict_multiple(beta,x):
    return np.matmul(x,beta).tolist()

def multiple_sum_of_squared_errors(beta, X, Y):
    return sum( (predict_multiple(beta,x) - y) ** 2 for x, y in zip(X,Y))[0,0]

def multiple_r_squared(beta,X,Y):
    return 1.0 - multiple_sum_of_squared_errors(beta, X, Y) / (total_sum_of_squares(Y)[0,0])
	
def approximate_derivative(f,x,dx=0.000001):
    try:
        approx = (f(x+dx) - f(x)) / dx
    except: 
        try:
            approx = (f(x) - f(x-dx)) / dx
        except:
            approx = float('nan')
    return approx
			
def component_f_at_v(f,x,v,i):
    newv = list(v)
    newv[i] = x
    return f(newv)
	
def approximate_gradient(f,v,dx=0.000001):
    grad = []
    for i in range(len(v)):
        cf = lambda x : component_f_at_v(f,x,v,i)
        approx = approximate_derivative(cf,v[i],dx)
        grad.append(approx)
    return grad
		
def quadratic_mapping(v,a,b,c):
    return [a*(x**2)+b*x+c for x in v]

def multivariate_gradient_descent(f, df, vstart, tolerance = 0.000001):
    H=[0.0000000001, 0.000000001, 0.00000001, 0.0000001, 0.000001, 0.00001, 0.0001, 0.001, 0.01, 0.1]
    v=vstart
    while True:
        fH=[f([v[i]+y for i,y in enumerate([-h*x for x in df(v)])]) for h in H]
        h=H[fH.index(min(fH))]
        newv=[v[i]+y for i,y in enumerate([-h*x for x in df(v)])]
        if ((abs(f(newv) - f(v))<tolerance) or (f(v)<=f(newv))) :
            break
        v = newv
    return v
	
if __name__ == "__main__":

    daily_minutes = [1,68.77,51.25,52.08,38.36,44.54,57.13,51.4,41.42,31.22,34.76,54.01,38.79,47.59,49.1,27.66,41.03,36.73,48.65,28.12,46.62,35.57,32.98,35,26.07,23.77,39.73,40.57,31.65,31.21,36.32,20.45,21.93,26.02,27.34,23.49,46.94,30.5,33.8,24.23,21.4,27.94,32.24,40.57,25.07,19.42,22.39,18.42,46.96,23.72,26.41,26.97,36.76,40.32,35.02,29.47,30.2,31,38.11,38.18,36.31,21.03,30.86,36.07,28.66,29.08,37.28,15.28,24.17,22.31,30.17,25.53,19.85,35.37,44.6,17.23,13.47,26.33,35.02,32.09,24.81,19.33,28.77,24.26,31.98,25.73,24.86,16.28,34.51,15.23,39.72,40.8,26.06,35.76,34.76,16.13,44.04,18.03,19.65,32.62,35.59,39.43,14.18,35.24,40.13,41.82,35.45,36.07,43.67,24.61,20.9,21.9,18.79,27.61,27.21,26.61,29.77,20.59,27.53,13.82,33.2,25,33.1,36.65,18.63,14.87,22.2,36.81,25.53,24.62,26.25,18.21,28.08,19.42,29.79,32.8,35.99,28.32,27.79,35.88,29.06,36.28,14.1,36.63,37.49,26.9,18.58,38.48,24.48,18.95,33.55,14.24,29.04,32.51,25.63,22.22,19,32.73,15.16,13.9,27.2,32.01,29.27,33,13.74,20.42,27.32,18.23,35.35,28.48,9.08,24.62,20.12,35.26,19.92,31.02,16.49,12.16,30.7,31.22,34.65,13.13,27.51,33.2,31.57,14.1,33.42,17.44,10.12,24.42,9.82,23.39,30.93,15.03,21.67,31.09,33.29,22.61,26.89,23.48,8.38,27.81,32.35,23.84]
    num_friends = [100,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

    print "\nComputing \"Best Fit\" quadratic curve mapping daily_minutes to num_friends.\n\n"

    print "Using matrix implementation of multiple least squares:\n"
    X = np.matrix([[x_i ** d for d in range(3)] for x_i in daily_minutes])
    Y = np.matrix(num_friends).T

	# This should produce approximately [26.7020, -1.6422, 0.0300], representing y = 0.0300x^2 - 1.6422x + 26.7020.
    beta = 	multiple_regression(X,Y) 
    print "beta = \n", beta

    print "\nUsing gradient descent implementation of multiple least squares:\n"

    f = lambda v: sum([(num_friends[i]-y)**2 for i,y in enumerate(quadratic_mapping(daily_minutes,v[0],v[1],v[2]))])
    df = lambda v: approximate_gradient(f,v)

	# This should produce (approximately) beta = [0.0054, 0.0322, 0.9979], representing y = 0.0054x^2 + 0.0322x + 0.9979.
    v=multivariate_gradient_descent(f,df,[0,0.25,1],0.01)
    print "beta=", v

