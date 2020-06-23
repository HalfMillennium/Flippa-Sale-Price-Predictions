# -*- coding: utf-8 -*-
"""
# Polynomial Regression

NOTE: 'listing_data_nospaces' contains 100 entries.

## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset"""

from sklearn.preprocessing import OneHotEncoder

dataset = pd.read_csv('listing_data_nospaces.csv')

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

print(X)

"""## Encoding categorical data"""

# for P-regression
from sklearn.preprocessing import PolynomialFeatures
#from sklearn.compose import ColumnTransformer

# Split dataset
arr_1 = X[:,0]
arr_2 = X[:,1]
arr_3 = X[:,3]
arr_4 = X[:,6]
arr_5 = X[:,9]
arr_6 = X[:,10]
arr_7 = X[:,11]
arr_8 = X[:,13]

# Categorical data
data_a = X[:,2]
data_b = X[:,4]
data_c = X[:,7]
data_d = X[:,8]
data_e = X[:,12]

# Convert categorical feature column to matrix of dummy variables
data_a = pd.get_dummies(data_a)
data_b = pd.get_dummies(data_b)
data_c = pd.get_dummies(data_c)
data_d = pd.get_dummies(data_d)
data_e = pd.get_dummies(data_e)

columns = [f'col_{num}' for num in range(1)]

df_1 = pd.DataFrame(data=arr_1,
          index=np.array(range(0, len(arr_1))),
          columns=['app_downloads_per_month'])
df_2 = pd.DataFrame(data=arr_2,
          index=np.array(range(0, len(arr_2))),
          columns=['average_profit'])
df_3 = pd.DataFrame(data=arr_3,
          index=np.array(range(0, len(arr_3))),
          columns=['buy_it_now_price'])
df_4 = pd.DataFrame(data=arr_4,
          index=np.array(range(0, len(arr_4))),
          columns=['listing_duration'])
df_5 = pd.DataFrame(data=arr_5,
          index=np.array(range(0, len(arr_5))),
          columns=['page_views_per_month'])
df_6 = pd.DataFrame(data=arr_6,
          index=np.array(range(0, len(arr_6))),
          columns=['profit_per_month'])
df_7 = pd.DataFrame(data=arr_7,
          index=np.array(range(0, len(arr_7))),
          columns=['asset_age'])
df_8 = pd.DataFrame(data=arr_8,
          index=np.array(range(0, len(arr_8))),
          columns=['uniques_per_month'])

#ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0,1,2])], remainder='passthrough')
#X = np.array(ct.fit_transform(X))
#X = pd.concat([data_column, X], axis=0)

final_encoded = pd.concat([data_a, data_b, data_c, data_d, data_e, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8], axis=1)
X = final_encoded

#Polynomial Features for P-regression
poly_reg = PolynomialFeatures(degree = 2)
X_poly = poly_reg.fit_transform(X)

"""## Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
print(X.isnull().sum().sum())

"""## Training the Polynomial Regression model on the Training set"""

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

poly_reg = PolynomialFeatures(degree = 3)
X_poly = poly_reg.fit_transform(X_train)

#regressor = LinearRegression()
#regressor.fit(X_train, y_train)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y_train)

"""## Predicting the Test set results"""

X_test_poly = poly_reg.fit_transform(X_test)
y_pred = lin_reg_2.predict(X_test_poly)
#y_pred = regressor.predict(X_test)
#np.set_printoptions(precision=3)

print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

plt.scatter(np.array(range(0, len(y_test))), y_test, color="red")
plt.scatter(np.array(range(0, len(y_pred))), y_pred, color="blue")
#plt.plot(X_test, lin_reg_2.predict(X_test_poly), color="blue")
plt.title('Predicted Price (Blue) vs Actual Price (Red)')
plt.xlabel('Prediction #')
plt.ylabel('Sale Price (US Dollars)')
plt.show()
