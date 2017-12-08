import pandas as pd
import numpy as np
import statsmodels.api as sm

df_adv = pd.read_csv('93cars.csv')
X = df_adv[['MinimumPrice','CityMPG','NumerOfCylinders','Horsepower','FuelTankCapacity','LuggageCapacity','EngineRevPerMile','Weight']
y = df_adv['EngineSize']
df_adv.head()


## fit a OLS model with intercept on TV and Radio
X = sm.add_constant(X)
est = sm.OLS(y, X).fit()

est.summary()