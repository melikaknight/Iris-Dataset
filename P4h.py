import pandas as pd
from sklearn.feature_selection import mutual_info_classif

Data_Raw = pd.read_csv('iris.data',sep=',',header=-1)

MI_Predicted = mutual_info_classif(Data_Raw[[0,1,2,3]].values,Data_Raw[4].values)

print(MI_Predicted)

