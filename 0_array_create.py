import numpy as np

# creating array

arr = np.array([23, 45, 23, 12])
arr

# check array types
type(arr)

# creating multidimension array
arr = np.array([[1, 4, 85, 45], [1, 14, 65, 45], [1, 4, 65, 5]])
arr

# slicing
arr = np.array([23, 56, 34, 22])
arr[0:3]
arr[2:3]

arr = np.array([[1, 4, 85, 45], [1, 14, 65, 45], [1, 4, 65, 5]])
arr[1, 2:4]
