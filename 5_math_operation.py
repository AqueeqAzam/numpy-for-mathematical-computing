import numpy as np
arr1 = np.array([34, 54, 20, 45, 90])
arr2 = np.array([4, 4, 23, 15, 10])

# add elements
add_ele = arr1 + 3
print(add_ele)

# add two array
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

# calculate square
arr1 = np.array([2, 5, 6])
arr2 = np.reciprocal(arr1)
print(arr2)

# calculate minimum
arr1 = np.array([2, 4, 6, 8, 10])
arr2 = np.min(arr1)
arr2

# calculate maxinium
arr1 = np.array([2, 4, 6, 8, 10])
arr2 = np.max(arr1)
arr2

# calculate minimum in 2 dim
arr1 = np.array([[2, 4, 6], [8, 10, 12]])
arr2 = np.min(arr1, axis=1)
arr2

# calculate minimum in 2 dim
arr1 = np.array([[2, 4, 6], [8, 10, 12]])
arr2 = np.min(arr1, axis=0)
arr2

# calculate trigonometry value
arr1 = np.array([0])
arr2 = np.sin(arr1)
arr2
arr3 = np.cos(arr1)
print(arr3)

# calculate minimum in 2 dim
arr1 = np.array([2, 4, 6])
arr2 = np.cumsum(arr1)
arr2

