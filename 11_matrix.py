import numpy as np
var = np.matrix([[1, 2], [4, 5]])
print(var)
print(type(var))

# transpose
var_t = np.transpose(var)
print(var_t)

# inverse
var_i = np.linalg.inv(var)
print(var_i)

# power
var_p = np.linalg.matrix_power(var, 2)
print(var_p)

# determinant
var_d = np.linalg.det(var)
print(var_d)
