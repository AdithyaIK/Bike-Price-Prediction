import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import joblib
#import seaborn as sns

dataset=pd.read_csv('Bike_Price_Prediction.csv')

from sklearn.preprocessing import OneHotEncoder,LabelEncoder


le=LabelEncoder()

dataset['Bike_company']=le.fit_transform(dataset['Bike_company'])
dataset['Bike_model']=le.fit_transform(dataset['Bike_model'])
dataset['Engine_type']=le.fit_transform(dataset['Engine_type'])
dataset['Fuel_type']=le.fit_transform(dataset['Fuel_type'])
dataset['CC(Cubic capacity)']=le.fit_transform(dataset['CC(Cubic capacity)'])

x=dataset.iloc[:,1:-2].values
y=dataset.iloc[:,-1].values

mean = math.floor(dataset['Engine_warranty'].mean())
x[:,4]=dataset['Engine_warranty'].fillna(mean)
x[np.isnan(x)]=np.median(x[~np.isnan(x)])
y[np.isnan(y)]=np.median(y[~np.isnan(y)])

from sklearn.tree import DecisionTreeRegressor
cls = DecisionTreeRegressor(random_state = 0)
cls.fit(x, y)

y_pred2=cls.predict(x)

from sklearn.metrics import r2_score
print(r2_score(y,y_pred2) *100)

#y_pred2=cls.predict([[10,9,2020,5,3,1,16]])
#print(y_pred2)

filename='Bikefinalized_model.sav'
joblib.dump(cls,filename)
