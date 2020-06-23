# -*- coding: utf-8 -*-
"""
# Support Vector Regression

NOTE: 'premium_four_hund' contains 400 entries.

## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset"""

from sklearn.preprocessing import OneHotEncoder

dataset = pd.read_csv('premium_four_hund.csv')

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
arr_4 = X[:,7]
arr_5 = X[:,8]
arr_6 = X[:,10]
arr_7 = X[:,11]
arr_8 = X[:,12]

# Categorical data
data_a = X[:,2]
data_b = X[:,4]
data_c = X[:,5]
data_d = X[:,6]
data_e = X[:,9]

# Convert categorical feature column to matrix of dummy variables
data_a = pd.get_dummies(data_a)
data_b = pd.get_dummies(data_b)
data_c = pd.get_dummies(data_c)
data_d = pd.get_dummies(data_d)
data_e = pd.get_dummies(data_e)

columns = [f'col_{num}' for num in range(1)]

"""# Feature Scaling"""

from sklearn.preprocessing import StandardScaler
sc_1 = StandardScaler()
arr_1 = sc_1.fit_transform(arr_1.reshape(len(arr_1),1))

sc_2 = StandardScaler()
arr_2 = sc_2.fit_transform(arr_2.reshape(len(arr_1),1))

sc_3 = StandardScaler()
arr_3 = sc_3.fit_transform(arr_3.reshape(len(arr_1),1))

sc_4 = StandardScaler()
arr_4 = sc_4.fit_transform(arr_4.reshape(len(arr_1),1))

sc_5 = StandardScaler()
arr_5 = sc_5.fit_transform(arr_5.reshape(len(arr_1),1))

sc_6 = StandardScaler()
arr_6 = sc_6.fit_transform(arr_6.reshape(len(arr_1),1))

sc_7 = StandardScaler()
arr_7 = sc_7.fit_transform(arr_7.reshape(len(arr_1),1))

sc_8 = StandardScaler()
arr_8 = sc_8.fit_transform(arr_8.reshape(len(arr_1),1))

y = y.reshape(len(y),1)
sc_y = StandardScaler()
y = sc_y.fit_transform(y)

"""# Finalizing Encoding"""

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
         columns=['page_views_per_month'])
df_5 = pd.DataFrame(data=arr_5,
          index=np.array(range(0, len(arr_5))),
          columns=['profit_per_month'])
df_6 = pd.DataFrame(data=arr_6,
          index=np.array(range(0, len(arr_6))),
          columns=['uniques_per_month'])
df_7 = pd.DataFrame(data=arr_7,
          index=np.array(range(0, len(arr_7))),
          columns=['asset_age'])
df_8 = pd.DataFrame(data=arr_8,
          index=np.array(range(0, len(arr_8))),
          columns=['listing_duration'])

X = final_encoded

print(X)

#print(y)

"""## Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
print(X.isnull().sum().sum())

"""## Training the SVR model on the Training set"""

from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X_train, y_train)

"""## Predicting the Test set results"""

results = sc_y.inverse_transform(regressor.predict(X_test));
#print(np.concatenate((results.reshape(len(results),1), sc_y.inverse_transform(y_test).reshape(len(y_test),1)),1))
acc = 0
for pred, act in zip(results, sc_y.inverse_transform(y_test)):
  if(abs(pred - act) <= 100 or abs(pred-act) <= (0.15*act)):
    acc = acc + 1

print(acc / len(y_test) * 100)

plt.scatter(np.array(range(0, 80)), sc_y.inverse_transform(y_test), color="red")
plt.scatter(np.array(range(0, 80)), results, color="blue")
plt.title('Sale Price Prediction (Blue) vs Actual Price (Red)')
plt.xlabel('Predictions')
plt.ylabel('Sale Price')
plt.show()
