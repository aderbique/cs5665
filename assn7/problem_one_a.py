#Austin Derbique
#A01967241

#Used http://dataaspirant.com/2014/12/20/linear-regression-implementation-in-python/
#For help with linear regression

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
from sklearn import datasets, linear_model

def oneA(fn):
    data = pd.read_csv(fn)
    x_param = []
    y_param = []
    for x,y in zip(data['CityMPG'],data['EngineSize']):
        x_param.append([float(x)])
        y_param.append(float(y))
    return x_param,y_param


# Function for Fitting data to Linear model
def linear_model_main(X_parameters,Y_parameters,predict_value):
    # Create linear regression object
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
    predict_outcome = regr.predict(predict_value)
    predictions = {}
    predictions['intercept'] = regr.intercept_
    predictions['coefficient'] = regr.coef_
    predictions['predicted_value'] = predict_outcome
    return predictions

def show_linear_line(X_parameters,Y_parameters):
    # Create linear regression object
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
    plt.scatter(X_parameters,Y_parameters,color='blue')
    plt.plot(X_parameters,regr.predict(X_parameters),color='red',linewidth=4)
    plt.xlabel('Engine Size')
    plt.ylabel('MPG')
    plt.title('Linear Regression model of Engine Size vs MPG')
    plt.xticks(())
    plt.yticks(())
    plt.show()


#One A
x,y = oneA('93cars.csv')
predict_value = 500
result = linear_model_main(x,y,predict_value)
print "Intercept value " , result['intercept']
print "coefficient" , result['coefficient']
print "Predicted value: ",result['predicted_value']
show_linear_line(x,y)

#One B

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


def oneB(fn):
    data = pd.read_csv(fn)
    x_param = []
    y_param = []
    for x1,x2,x3,x4,x5,x6,x7,x8,y in zip(data['MinimumPrice'],data['CityMPG'],data['NumberOfCylinders'],data['Horsepower'],data['FuelTankCapacity'],data['LuggageCapacity'],data['EngineRevPerMile'],data['Weight'],data['EngineSize']):
        y_param.append([float(y)])
        x_list = [float(x1),float(x2),float(x3),float(x4),float(x5),float(x6),float(x7),float(x8)]
        x_param.append(x_list)

    flatlist = []
    for sublist in x_param:
    	for item in sublist:
    		flatlist.append([item])
    return flatlist,y_param

x,y = oneB('93cars.csv')
predict_value = 500
result = linear_model_main(x,y,predict_value)
print "Intercept value " , result['intercept']
print "coefficient" , result['coefficient']
print "Predicted value: ",result['predicted_value']
regr = linear_model.LinearRegression()
regr.fit(X_parameters, Y_parameters)
plt.scatter(X_parameters,Y_parameters,color='blue')
plt.plot(X_parameters,regr.predict(X_parameters),color='red',linewidth=4)
plt.xlabel('Engine Size')
plt.ylabel('MPG')
plt.title('Linear Regression model of Engine Size vs MPG')
plt.xticks(())
plt.yticks(())
plt.show()



"""
csv = np.genfromtxt ('93cars.csv', delimeter=",")
print csv


# Load the dataset dataset
dataset = datasets.load_dataset()

# Use only one feature
dataset_X = dataset.data[:, np.newaxis, 2]

# Split the data into training/testing sets
dataset_X_train = dataset_X[:-20]
dataset_X_test = dataset_X[-20:]

# Split the targets into training/testing sets
dataset_y_train = dataset.target[:-20]
dataset_y_test = dataset.target[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(dataset_X_train, dataset_y_train)

# Make predictions using the testing set
dataset_y_pred = regr.predict(dataset_X_test)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(dataset_y_test, dataset_y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(dataset_y_test, dataset_y_pred))

# Plot outputs
plt.scatter(dataset_X_test, dataset_y_test,  color='black')
plt.plot(dataset_X_test, dataset_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()

"""