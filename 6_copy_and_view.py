import numpy as np

arr = np.array([3, 6, 9, 12])
co = arr.copy()
arr[1] = 30
print('Original', arr)
print('Copy', co)

# view
vi = arr.view()
arr[1] = 40
print('Original', arr)
print('View', vi)
