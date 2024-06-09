import numpy as np

# concatenate array
arr1 = np.array([34, 67, 90])
arr2 = np.array([3, 6, 1])
arr3 = np.concatenate([arr1, arr2])
arr3

# concatenate array in 2-d
arr1 = np.array([[34, 7], [90, 1]])
arr2 = np.array([[3, 6], [1, 12]])

# concatnating 2-d array
arr3 = np.concatenate((arr1, arr2))
print(arr3)

# merging array
arr3 = np.concatenate((arr1, arr2), axis=1)
print(arr3)

# horizontal concatenation
hor_cat = np.hstack([arr1, arr2])
hor_cat

# vertical concatenation
ver_cat = np.vstack([arr1, arr2])
ver_cat

# spelliting array
a = np.array([34, 23, 2, 6, 8, 80, 34, 23, 12, 80])
b = np.array_split(a, 3)
print(b)
