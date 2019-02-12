import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

Data_Raw = pd.read_csv('iris.data',sep=',',header=-1)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
data_2d = Data_Raw.values[:,0:1]
data_array = np.array(data_2d)
x_data, y_data = np.meshgrid( np.arange(data_array.shape[1]), np.arange(data_array.shape[0]) )
x_data = x_data.flatten()
y_data = y_data.flatten()
z_data = data_array.flatten()
ax.bar3d( x_data,y_data, np.zeros(len(z_data)),1, 1, z_data )
plt.xlabel('Var1')
plt.ylabel('Var2')
plt.title('3D Histogram of data')
plt.show()