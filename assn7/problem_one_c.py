#help from http://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_and_elasticnet.html#sphx-glr-auto-examples-linear-model-plot-lasso-and-elasticnet-py
import pandas as pd
import numpy as np
import statsmodels.api as sm

print(__doc__)

import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import r2_score


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


#One A
X,y = oneA('93cars.csv') 
  
 
  
## Generate some sparse data to play with
np.random.seed(100)
#
n_samples, n_features = 25, 150
X = np.random.randn(n_samples, n_features)
coef = 3 * np.random.randn(n_features)
inds = np.arange(n_features)
np.random.shuffle(inds)
coef[inds[10:]] = 0  # sparsify coef

y = np.dot(X, coef)

# add noise
y += 0.01 * np.random.normal(size=n_samples)




# Split data in train set and test set
n_samples = X.shape[0]
X_train, y_train = X[:n_samples // 2], y[:n_samples // 2]
X_test, y_test = X[n_samples // 2:], y[n_samples // 2:]

# #############################################################################
# Lasso
from sklearn.linear_model import Lasso

alpha = 0.1
lasso = Lasso(alpha=alpha)

y_pred_lasso = lasso.fit(X_train, y_train).predict(X_test)
r2_score_lasso = r2_score(y_test, y_pred_lasso)
print(lasso)
print("Lasso Regression of Coefficients related to Engine Size")


plt.plot(lasso.coef_, color='gold', linewidth=2,
         label='Lasso coefficients')
plt.plot(coef, '--', color='navy', label='original coefficients')
plt.xlabel('Engine Size')
plt.ylabel('Coeffecients Lasso Regression')
plt.legend(loc='best')
plt.title("Lasso Regression of Coefficients related to Engine Size")
plt.show()

#df_adv = pd.read_csv('93cars.csv')
#X = df_adv[['MinimumPrice','CityMPG','NumerOfCylinders','Horsepower','FuelTankCapacity','LuggageCapacity','EngineRevPerMile','Weight']
#y = df_adv['EngineSize']
#df_adv.head()


## fit a OLS model with intercept on TV and Radio
#X = sm.add_constant(X)
#est = sm.OLS(y, X).fit()

#est.summary()


print('finished!')