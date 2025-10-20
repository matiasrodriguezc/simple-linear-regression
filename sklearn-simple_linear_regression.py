# For these lessons we will need NumPy, pandas, matplotlib and seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# and of course the actual regression (machine learning) module
from sklearn.linear_model import LinearRegression


#%%
# We start by loading the data
data = pd.read_csv('1.01. Simple linear regression.csv')
# Let's explore the top 5 rows of the df
data.head()


#%%Create the Regression
# There is a single independent variable: 'SAT'
x = data['SAT']
# and a single depended variable: 'GPA'
y = data['GPA']
# Often it is useful to check the shapes of the features
x.shape
y.shape
# In order to feed x to sklearn, it should be a 2D array (a matrix)
# Therefore, we must reshape it 
# Note that this will not be needed when we've got more than 1 feature (as the inputs will be a 2D array by default)
# x_matrix = x.values.reshape(84,1)
x_matrix = x.values.reshape(-1,1)
# Check the shape just in case
x_matrix.shape


#%%Regression itself
# We start by creating a linear regression object
reg = LinearRegression()
# The whole learning process boils down to fitting the regression
# Note that the first argument is the independent variable, while the second - the dependent (unlike with StatsModels)
reg.fit(x_matrix,y)


#%%R-Squared
# To get the R-squared in sklearn we must call the appropriate method
reg.score(x_matrix,y)


#%%Coefficients
# Getting the coefficients of the regression
# Note that the output is an array, as we usually expect several coefficients
reg.coef_


#%%Intercept
# Getting the intercept of the regression
# Note that the result is a float as we usually expect a single value
reg.intercept_


#%%Making predictions
# There is a dedicated method should we want to predict values
# Note that the result is an array, as we can predict more than one value at a time
reg.predict(1740)
# we can create a pandas data frame with several different values of SAT
new_data = pd.DataFrame(data=[1740,1760],columns=['SAT'])
new_data
# We can predict the whole data frame in bulk
# Note that the result is an array, this time with 2 elements
reg.predict(new_data)


#%%Finally, we can directly store the predictions in a new series of the same dataframe
new_data['Predicted_GPA'] = reg.predict(new_data)
new_data


#%%
# There are different ways to plot the data - here's the matplotlib code
plt.scatter(x,y)

# Parametrized version of the regression line
yhat = reg.coef_*x_matrix + reg.intercept_

# Non-parametrized version of the regression line
#yhat = 0.0017*x + 0.275

# Plotting the regression line
fig = plt.plot(x,yhat, lw=4, c='orange', label ='regression line')

# Labelling our axes
plt.xlabel('SAT', fontsize = 20)
plt.ylabel('GPA', fontsize = 20)
plt.show()