import numpy as np

#similar as for loop 
a = np.arange(1,100,2)
print(a)

a = a.reshape((10,5))
print(a)

# a = a.flatten()
# print(a)

print(a.ravel())