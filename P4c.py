import pandas as pd
import matplotlib.pyplot as plt

Data_Raw = pd.read_csv('iris.data',sep=',',header=-1)


Unique_Label = pd.unique(Data_Raw.values[:,4])
NUmeric_Label = Data_Raw[4].apply(list(Unique_Label).index)
count = 0
colors = ['red','green','blue','purple']
for i in Unique_Label:
    Temp = Data_Raw[(Data_Raw[4]==i)][[0,1]]
    plt.scatter(Temp[:][0],Temp[:][1], marker='^', c=colors[count], label = i)
    count = count +1
plt.legend()
plt.xlabel('Var1')
plt.ylabel('Var2')
plt.show()