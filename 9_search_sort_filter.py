import numpy as np

arr = np.array([23, 90, 67, 8, 5, 8, 5])

# searchimh fun
arr_sea = np.where(arr == 67)

arr_sea = np.where(arr % 2 == 0)
print(arr_sea)

# search sorting fun
arr = np.array([23, 90, 67, 8, 5, 8, 5])
arr_sea_sort = np.searchsorted(arr, 8)
print(arr_sea_sort)

# sorting fun
arr = np.array([23, 90, 67, 8, 5, 8, 5])
arr_sort = np.sort(arr)
print(arr_sort)

# filter fun
arr = np.array([23, 90, 67])
f = [True, False, True]
new_arr = arr[f]
print(new_arr)
