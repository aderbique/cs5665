import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from patsy import dmatrices
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.cross_validation import cross_val_score

def readfile(fn):
    data = pd.read_csv(fn)
    x_param = []
    y_param = []
    for x,y in zip(data['CityMPG'],data['EngineSize']):
        x_param.append([float(x)])
        y_param.append(float(y))
    return x_param,y_param


# load dataset
dta = sm.datasets.fair.load_pandas().data

# add "affair" column: 1 represents having affairs, 0 represents not
dta['EngineSize'] = (dta.size > 0).astype(int)

# create dataframes with an intercept column and dummy variables for
# occupation and occupation_husb

print X.columns

# flatten y into a 1-D array
y = np.ravel(y)

# instantiate a logistic regression model, and fit with X and y
model = LogisticRegression()
model = model.fit(X, y)

# check the accuracy on the training set
model.score(X, y)

# what percentage had affairs?
y.mean()

# examine the coefficients
pd.DataFrame(zip(X.columns, np.transpose(model.coef_)))