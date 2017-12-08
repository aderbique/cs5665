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
import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model, decomposition, datasets
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

df_adv = pd.read_csv('93cars.csv')
X = df_adv[['MinimumPrice','CityMPG','NumerOfCylinders','Horsepower','FuelTankCapacity','LuggageCapacity','EngineRevPerMile','Weight']
y = df_adv['EngineSize']
df_adv.head()




logistic = linear_model.LogisticRegression()

pca = decomposition.PCA()
pipe = Pipeline(steps=[('pca', pca), ('logistic', logistic)])

digits = datasets.load_digits()
X_digits = digits.data
y_digits = digits.target

# Plot the PCA spectrum
pca.fit(X_digits)

plt.figure(1, figsize=(4, 3))
plt.clf()
plt.axes([.2, .2, .7, .7])
plt.plot(pca.explained_variance_, linewidth=2)
plt.axis('tight')
plt.xlabel('n_components')
plt.ylabel('explained_variance_')

# Prediction
n_components = [20, 40, 64]
Cs = np.logspace(-4, 4, 3)

# Parameters of pipelines can be set using '___' separated parameter names:
estimator = GridSearchCV(pipe,dict(pca__n_components=n_components,logistic__C=Cs))
estimator.fit(X_digits, y_digits)

plt.axvline(estimator.best_estimator_.named_steps['pca'].n_components,linestyle=':', label='n_components chosen')
plt.legend(prop=dict(size=12))
plt.show()
