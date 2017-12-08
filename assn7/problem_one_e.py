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
    for x,y in zip(data['Type'],data['Horsepower']):
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
    plt.ylabel('Size')
    plt.title('Logistic Regression model of Engine Size vs Size')
    plt.xticks(())
    plt.yticks(())
    plt.show()


#One A
x,y = oneA('93cars_e.csv')
predict_value = 500
result = linear_model_main(x,y,predict_value)
print "Intercept value " , result['intercept']
print "coefficient" , result['coefficient']
print "Predicted value: ",result['predicted_value']
show_linear_line(x,y)