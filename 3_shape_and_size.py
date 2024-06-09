import numpy as np

var = np.array([[1, 4], [3, 6]])
print(var)

# check dimension
print(var.shape)

# creating multidimension array
var1 = np.array([1, 3, 6, 8, 19], ndmin=4)
print(var1)
print(var1.ndim)
print(var1.shape)

# reshape array
var3 = np.array([1, 2, 3, 4, 5, 6])
x = var3.reshape(2, 3)
print(x)


var4 = np.array([1, 2, 3, 4, 5, 6])
x = var4.reshape(-1)
print(x)
print(x.ndim)

