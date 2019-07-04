# DayEight_DS

import pandas as pd numpy as np
data =np.array(['a','b','c','d'])
s=pd.Series(data,index=[10,20,30,40])
print(s)

output
10    a
20    b
30    c
40    d
dtype: object
simply say that Series and index values

Adding a new column to an existing DataFrame object with column label by passing new series

using pop function

print ("Deleting another column using POP function:")

df.pop('two') # pop means pop the last Element of the list

print (df)

Matplotlib is plot the graph
import matplotlib.pyplot as plt  



# Compute the x and y coordinates for points on a sine curve 

x = np.arange(0, 3 * np.pi, 0.1) 

y = np.sin(x) 

plt.title("sine wave form") #  plt .title means that title of the bar and graph 



# Plot the points using matplotlib 

plt.plot(x, y) # plt.plot directly plot the graph

plt.show() # show() means show the graph in the jupyter notebook




