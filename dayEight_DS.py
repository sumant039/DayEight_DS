import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[10,20,30,40])
print (s)

#A dict can be passed as input and if no index is specified, then the dictionary keys are taken in a sorted order to construct index.
#If index is passed, the values in data corresponding to the labels in the index will be pulled out.
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
print (s)


s= pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve the first element
print (s[0])


#Dataframe

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,30]}
df = pd.DataFrame(data)
print (df)
df.to_excel("output.xlsx")


#Column Addition


d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df1 = pd.DataFrame(d)

# Adding a new column to an existing DataFrame object with column label by passing new series

print ("Adding a new column by passing as Series:")
df1['three']=pd.Series([10,20,30],index=['a','b','c'])
print (df1)

print ("Adding a new column using the existing columns in DataFrame:")
df1['four']=df1['one']+df1['three']

print (df1)


#Deleting data from Pandas
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']), 
   'three' : pd.Series([10,20,30], index=['a','b','c'])}

df = pd.DataFrame(d)
print ("Our dataframe is:")
print (df)




# using del function
print ("Deleting the first column using DEL function:")
del df['one']
print (df)

# using pop function
print ("Deleting another column using POP function:")
df.pop('two')
print (df)


#Access row of DataFrame
print(df.loc['a'])


#Slice Rows

print (df[2:4])


df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

print(df)
print(df2)
    
df = df.append(df2)

print("After append")

print(df)

# Drop rows with label 0
df = df.drop(0)
print("After dropping row labelled 0")
print (df)



data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
   'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print (p['Item1'])

print(p['Item2'])


#Access elements based on major and minor

print (p.major_xs(1))

print("Minor Axis:")
print (p.minor_xs(1))






#Matplotlib


import matplotlib.pyplot as plt  

# Compute the x and y coordinates for points on a sine curve 
x = np.arange(0, 3 * np.pi, 0.1) 
y = np.sin(x) 
plt.title("sine wave form") 

# Plot the points using matplotlib 
plt.plot(x, y) 
plt.show() 





