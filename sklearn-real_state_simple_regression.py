#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.linear_model import LinearRegression


#%%Load the data
data = pd.read_csv('real_estate_price_size.csv')
data.head()
data.describe()

#%%Create the Regression
x = data['size']
y = data['price']


#%%Explore the Data
plt.scatter(x,y)
plt.xlabel('Size',fontsize=20)
plt.ylabel('Price',fontsize=20)
plt.show()

#%% Transform the inputs into a matrix (2D object)
x_matrix = x.values.reshape(-1,1)


#%%Regression itself
reg = LinearRegression()
reg.fit(x_matrix,y)

#%%Calculate the R-Squared
reg.score(x_matrix,y)


#%%Find the intercept
reg.intercept_


#%%Find the coefficients
reg.coef_


#%%Making predictions
reg.predict(750)