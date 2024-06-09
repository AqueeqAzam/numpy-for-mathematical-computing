import numpy as np

# appending
arr = np.array([23, 90, 67, 8, 5, 8, 54])
np.append(arr, [50, 100])

# inserting
np.insert(arr, 1, [200, 300])


# Fix: Create an array with consistent row lengths
arr = np.array([[23, 90, 67], [8, 5, 8]])  # Removed the extra element from the second row
np.insert(arr, 1, [200, 300], axis=1)

# deleting
arr_del = np.array([23, 90, 67, 8, 5, 8, 54])
np.delete(arr_del, 1)

np.delete(arr_del, 1, axis=0)
