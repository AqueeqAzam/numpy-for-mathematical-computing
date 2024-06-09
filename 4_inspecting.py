import numpy as np

# creating array
arr = np.array([23, 45, 23, 12])
arr

# check array types
type(arr)

# creating multidimension array
arr = np.array([[1, 4, 85, 45], [1, 14, 65, 45], [1, 4, 65, 5]])
arr

# check dimension (no of array dim)
arr.ndim

# slicing
arr = np.array([23, 56, 34, 22])
arr[0:3]
arr[2:3]

# second example
arr = np.array([[1, 4, 85, 45], [1, 14, 65, 45], [1, 4, 65, 5]])
arr[1, 2:4]

# check size (no of array ele)
np.size(arr)

# checking length
len(arr)

# check data types
arr.dtype

arr.astype
