import numpy as np
var = np.array([1,2,3,4])
print("Data", var.dtype)

var = np.array([1.3,2.6,3.8,4.2])
print("Data", var.dtype)

var = np.array(['A', 'V', 'X'])
print("Data", var.dtype)

# converting datatypes
var = np.array([1,2,3,4], dtype = np.int8)
print("Data Type", var.dtype)

var = np.array([1,2,3,4], dtype = "f")
print("Data Type", var.dtype)
print(var)
