import numpy as np

# 📌 21. Broadcasting & Vectorized Operations
# Definition: Broadcasting allows arrays of different shapes to be used together without explicit loops.
# Usage: Used in image processing, ML tensor computations, and numerical simulations.

arr1 = np.array([[1], [2], [3]])  # 3x1 matrix
arr2 = np.array([10, 20, 30])  # 1x3 matrix

# Automatically expands shapes and adds element-wise
broadcasted_sum = arr1 + arr2  
print("\n📡 Broadcasted Addition:\n", broadcasted_sum)  # Each row adds corresponding elements


# 📌 22. Advanced Indexing & Slicing (Fancy Indexing, Boolean Masks)
# Definition: Fancy indexing allows selecting multiple elements at once, and boolean masks filter data.
# Usage: Used in data filtering, outlier detection, and dataset cleaning.

arr = np.array([10, 20, 30, 40, 50])

# Fancy Indexing (Select multiple elements)
selected = arr[[0, 2, 4]]
print("🎯 Selected Elements (Fancy Indexing):", selected)  # Picks elements at indices 0, 2, and 4

# Boolean Masking (Filter elements greater than 25)
mask = arr > 25
filtered_arr = arr[mask]
print("🔍 Filtered Elements (Boolean Masking):", filtered_arr)  # Keeps values > 25


# 📌 23. Performance Comparison (NumPy vs Python List)
# Definition: NumPy operations are significantly faster than Python lists due to optimized C-based execution.
# Usage: Used in performance-critical applications like AI and large-scale data analysis.

import time

size = 1_000_000  # Large array size
list_data = list(range(size))
numpy_data = np.arange(size)

# Measure Python list computation time
start = time.time()
list_result = [x * 2 for x in list_data]  # List comprehension
end = time.time()
print("\n🐢 Python List Time:", end - start, "seconds")

# Measure NumPy computation time
start = time.time()
numpy_result = numpy_data * 2  # Vectorized operation
end = time.time()
print("🚀 NumPy Time:", end - start, "seconds")  # Much faster


# 📌 24. Working with Real Datasets (Loading CSV Files)
# Definition: NumPy can read CSV files and convert them into structured arrays.
# Usage: Used in data analysis, ML preprocessing, and handling structured data.

# CSV Example (Assume a file 'data.csv' exists with numbers)
# Uncomment the next line if you have a CSV file to read
# dataset = np.genfromtxt('data.csv', delimiter=',', skip_header=1)

# Creating a mock dataset for demonstration
dataset = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("\n📊 Loaded CSV Data (Mock Data):\n", dataset)


# 📌 25. Fourier Transform & Linear Algebra (Eigenvalues, Inverse Matrices)
# Definition: NumPy provides fast implementations of Fourier Transforms and matrix operations.
# Usage: Used in signal processing, physics, and AI algorithms.

# Fourier Transform (Frequency domain analysis)
signal = np.array([1, 2, 1, -1, -2, -1])
fft_result = np.fft.fft(signal)
print("\n📡 Fourier Transform (FFT):\n", fft_result)

# Eigenvalues & Eigenvectors (Linear Algebra)
matrix = np.array([[4, 2], [3, 1]])
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("📏 Eigenvalues:", eigenvalues)
print("📐 Eigenvectors:\n", eigenvectors)

# Inverse of a Matrix
matrix_inverse = np.linalg.inv(matrix)
print("🔄 Inverse Matrix:\n", matrix_inverse)
