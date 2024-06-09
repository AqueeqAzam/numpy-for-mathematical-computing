# shuffle function
import numpy as np
var = np.array([1, 2, 3, 4, 5])
np.random.shuffle(var)
print(var)

# unique function
var1 = np.array([1, 2, 3, 4, 5, 6, 3, 5, 2])
x = np.unique(var1)
print(x)

# size function
var2 = np.array([1, 2, 3, 4, 5, 6, 3, 5, 2])
x = np.size(var2)
print(x)

# resize function
var2 = np.array([1, 2, 3, 4, 5, 6, 3, 5, 2])
x = np.resize(var2, (3, 3))
print(x)

# flatten function
var2 = np.array([1, 2, 3, 4, 5, 6, 3, 5, 2])
x = np.resize(var2, (3, 2))
print(x.flatten(order='F'))
