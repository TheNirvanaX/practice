# %%
import pandas as pd
import numpy as np

# %%
file_path='F:/programming/dataset/titanic/train.csv'
df=pd.read_csv(file_path)
df.describe()

# %%
#feature
features=['Pclass','Age','SibSp','Parch','Fare']

#dependent and independent varibale
y=df.Survived
X=df[features].values
print(X)

# %%

#import testdataset
file_path_='F:/programming/dataset/titanic/test.csv'
testset=pd.read_csv(file_path_)
_test=testset[features].values
print(test_X)

# %%
#missing values
from sklearn.impute import SimpleImputer
se=SimpleImputer(missing_values=np.nan,strategy='mean')
se=se.fit(X[:,1:2])
X[:,1:2]=se.transform(X[:,1:2])
se=SimpleImputer(missing_values=np.nan,strategy='mean')
se=se.fit(test_X[:,1:2])
test_X[:,1:2]=se.transform(test_X[:,1:2])
print(X)
print(test_X)

# %%
#split data into train and validation set
from sklearn.model_selection import train_test_split
train_X,val_X,train_y,val_y=train_test_split(X,y,random_state=0)

# %%
#model
from sklearn.ensemble import RandomForestRegressor
model=RandomForestRegressor(random_state=1)
#fit model
model.fit(train_X,train_y)

# %%
#predict
val_pred=model.predict(val_X)

# %%
#mae
from sklearn.metrics import mean_absolute_error
val_mae=mean_absolute_error(val_y,val_pred)
print(val_mae)

# %%
#predict all
model=RandomForestRegressor(random_state=1)
model.fit(X,y)

# %%
#predict on test set
y_out=model.predict(test_X)

# %%


# %%



