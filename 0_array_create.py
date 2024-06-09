import numpy as np

# creating array

arr = np.array([23, 45, 23, 12])
arr

# check array types
type(arr)

# zeros array (fill array with zeros)
arr_zero = np.zeros(4)
arr_zero

# with multi dimension
arr_zero = np.zeros((3,4))
arr_zero

# ones array (fill array with zeros)
arr_ones = np.ones(4)
arr_ones

# empty array
arr_em = np.empty(4)
arr_em

# array range
arr_rn = np.arange(4)
arr_rn

# array dimgonal
arr_dig = np.eye(3, 5)
arr_dig

# array linespace
arr_lp = np.linspace(0, 20, num=5)
arr_lp
