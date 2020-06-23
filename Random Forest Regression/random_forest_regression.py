# -*- coding: utf-8 -*-
"""
# Support Vector Regression

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

"""# Finalizing Encoding (converting arrays back to dataframes)"""

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

final_encoded = pd.concat([data_a, data_b, data_c, data_d, data_e, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8], axis=1)
X = final_encoded

"""## Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.6, random_state = 0)
print(X.isnull().sum().sum())

"""## Training the SVR model on the Training set"""

from sklearn.ensemble import RandomForestRegressor   # RANDOM FOREST (compilation of decision trees)
regressor = RandomForestRegressor(random_state = 15)
regressor.fit(X_train, y_train)

"""## Predicting the Test set results"""

results = regressor.predict(X_test);
#print(np.concatenate((results.reshape(len(results),1), y_test.reshape(len(y_test),1)),1))
acc = 0
for pred, act in zip(results, y_test):
  if(abs(pred - act) <= 100 or abs(pred-act) <= (0.15*act)):
    acc = acc + 1

print(acc / len(y_test) * 100)

plt.plot(np.array(range(0, len(y_test))), y_test, color="red")
plt.plot(np.array(range(0, len(y_test))), results, color="blue")
plt.title('Sale Price Prediction (Blue) vs Actual Price (Red)')
plt.xlabel('Predictions')
plt.ylabel('Sale Price')
plt.show()
