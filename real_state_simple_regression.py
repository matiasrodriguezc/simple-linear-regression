#%%
#Real estate is one of those examples that every regression course goes through as it is extremely easy to understand and there is a (almost always) certain causal relationship to be found.
#The data is located in the file: 'real_estate_price_size.csv'. 
#You are expected to create a simple linear regression (similar to the one in the lecture), using the new data.
#In this exercise, the dependent variable is 'price', while the independent variable is 'size'.


#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set()


#%%Load the Data
data = pd.read_csv('real_estate_price_size.csv')
data.head()
data.describe()


#%%Create the regression
### Declare the dependent and the independent variables
y = data['price']
x1 = data['size']


#%%Explore the Data
plt.scatter(x1,y)
plt.xlabel('Size',fontsize=20)
plt.ylabel('Price',fontsize=20)
plt.show()


#%%Regression itself
x = sm.add_constant(x1)
results = sm.OLS(y,x).fit()
results.summary()


#%%
plt.scatter(x1,y)
yhat = x1*223.1787+101900
fig = plt.plot(x1,yhat, lw=4, c='orange', label ='regression line')
plt.xlabel('Size', fontsize = 20)
plt.ylabel('Price', fontsize = 20)
plt.show()
# %%
