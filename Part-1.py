import numpy as np

lst  = np.array( [1,2,3,4])
print(lst)


# 1-d array
b = np.array([1,3,2,4,5])
print(b)

#2-d array
c = np.array([[1,3,2,4],[3,54,66,32]])
print(c)

#3-d array
d = np.array([[[1,2],
               [3,4],
               [3,4]]])
print(d)


print(type(d))
print(c.size) 
print(d.shape)  
print(d.dtype)  #data type of element inside array
print(d.transpose()) #to calculate transpose 