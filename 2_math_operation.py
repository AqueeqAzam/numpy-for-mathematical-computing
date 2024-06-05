import numpy as np
arr1 = np.array([34, 54, 20, 45, 90])
arr2 = np.array([4, 4, 23, 15, 10])

arr = arr1 + arr2
arr

# by using add function
arr_add = np.add(arr1, arr2)
arr_add

# by using subtract function
arr_sub = np.subtract(arr1, arr2)
arr_sub

# by using multiply function
arr_mul = np.multiply(arr1, arr2)
arr_mul

# by using subtract function
arr_div = np.divide(arr1, arr2)
arr_div



arr1 = np.array([[34, 54], [20, 45]])  # Modified to have consistent dimensions
arr2 = np.array([[4, 4], [23, 15]])    # Modified to have consistent dimensions
mul_dim_arr_add = np.add(arr1, arr2)
mul_dim_arr_add

# calculate power
arr1 = np.array([3, 5, 6, 8])
arr2 = np.array([3])
np.power(arr1, arr2)

# calculate squareroot
arr1 = np.array([27, 125, 16])
arr2 = np.sqrt(arr1)
arr2

# calculate square
arr1 = np.array([27, 125, 16])
arr2 = np.square(arr1)
arr2


