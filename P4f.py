import pandas as pd
import numpy as np

Data_Raw = pd.read_csv('iris.data',sep=',',header=-1)

# >>>>>>>>>>>>> Cov Matrix

Unique_Label = pd.unique(Data_Raw.values[:,4])
Class1 = Data_Raw[(Data_Raw[4]==Unique_Label[0])].values[:,0:4]
Class2 = Data_Raw[(Data_Raw[4]==Unique_Label[1])].values[:,0:4]

Class1_Normalized = Class1 - np.mean(Class1)
Class2_Normalized = Class2 - np.mean(Class2)
Cov_Mat = [[0,0],[0,0]]
Cov_Mat[0][0] = np.sum((np.multiply(Class1_Normalized,Class1_Normalized))/(np.size(Class1_Normalized)-1))
Cov_Mat[0][1] = np.sum((np.multiply(Class1_Normalized,Class2_Normalized))/(np.size(Class1_Normalized)-1))
Cov_Mat[1][0] = np.sum((np.multiply(Class2_Normalized,Class1_Normalized))/(np.size(Class1_Normalized)-1))
Cov_Mat[1][1] = np.sum((np.multiply(Class2_Normalized,Class2_Normalized))/(np.size(Class1_Normalized)-1))

Corr_Mat = Cov_Mat / (np.std(Class1)*np.std(Class2))
[Corr_Mat[0][0],Corr_Mat[1][1]] = [round(Corr_Mat[0][0]),round(Corr_Mat[1][1])]

print(Corr_Mat)