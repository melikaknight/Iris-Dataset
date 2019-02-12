import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


Data_Raw = pd.read_csv('iris.data',sep=',',header=-1)


Means = Data_Raw[Data_Raw[4]=='Iris-virginica'].mean()
Std  = Data_Raw[Data_Raw[4]=='Iris-virginica'].std()
import matplotlib.mlab as mlab

for i in range(0,4,1):
    x = np.linspace(Means[i] - 3*Std[i], Means[i] + 3*Std[i], 100)
    plt.plot(x,mlab.normpdf(x, Means[i], Std[i]))
plt.legend(['Variable 1','Variable 2','Variable 3','Variable 4'])

Corr_Of_Features = np.corrcoef((Data_Raw[[0,1,2,3]][Data_Raw[4]=='Iris-virginica']),rowvar=False)
print(Corr_Of_Features)

plt.show()