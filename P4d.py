import pandas as pd
import matplotlib.pyplot as plt

Data_Raw = pd.read_csv('iris.data',sep=',',header=-1)

Mean_Arr = Data_Raw.mean().values
Var_Arr = Data_Raw.var().values
index = ['Var1', 'Var2', 'Var3' , 'Var4']
Data_Frame_Obj =  pd.DataFrame({'Mean': Mean_Arr,'Variance': Var_Arr}, index=index)

Plot_Obj = Data_Frame_Obj.plot.bar(rot=0)
axes = Data_Frame_Obj.plot.bar(rot=0, subplots=True)
axes[1].legend(loc=2)

plt.show()