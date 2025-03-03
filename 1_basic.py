import numpy as np

# 📌 1. Creating NumPy Arrays
# Definition: NumPy arrays are used to store multiple values in a single variable.
# Usage: Used in scientific computing, data analysis, and machine learning.
arr = np.array([1, 2, 3, 4, 5])
print("🌟 NumPy Array:", arr)


# 📌 2. Checking NumPy Version
# Definition: Shows the installed version of NumPy.
# Usage: Ensures compatibility in data science projects.
print("📌 NumPy Version:", np.__version__)


# 📌 3. Creating Arrays with Specific Types
# Definition: NumPy allows specifying the data type of arrays.
# Usage: Used in memory optimization, scientific calculations.
float_arr = np.array([1, 2, 3], dtype=float)
print("🔢 Float Array:", float_arr)


# 📌 4. Generating Arrays with Zeros, Ones, and Random Numbers
# Definition: Creates arrays filled with zeros, ones, or random values.
# Usage: Used in initializing weights in AI models, placeholders in ML.
zeros = np.zeros((2, 3))
ones = np.ones((3, 3))
rand_nums = np.random.rand(2, 2)
print("⭕ Zeros Array:\n", zeros)
print("🔲 Ones Array:\n", ones)
print("🎲 Random Array:\n", rand_nums)


# 📌 5. Generating a Range of Numbers
# Definition: Creates an array with evenly spaced values.
# Usage: Used in graphs, mathematical sequences, simulations.
range_arr = np.arange(1, 10, 2)  # Start=1, Stop=10, Step=2
print("📏 Range Array:", range_arr)


# 📌 6. Reshaping Arrays
# Definition: Changes the shape of an array without changing its data.
# Usage: Used in deep learning, image processing.
reshaped_arr = np.arange(1, 10).reshape(3, 3)
print("🔄 Reshaped Array:\n", reshaped_arr)


# 📌 7. Basic Array Operations (Addition, Multiplication)
# Definition: NumPy allows element-wise operations on arrays.
# Usage: Used in signal processing, AI computations.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
sum_arr = a + b
product_arr = a * b
print("➕ Sum:", sum_arr)
print("✖️ Product:", product_arr)


# 📌 8. Matrix Multiplication (Dot Product)
# Definition: Computes the dot product of two matrices.
# Usage: Used in AI, physics simulations, and linear algebra.
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
dot_product = np.dot(matrix1, matrix2)
print("🔗 Dot Product:\n", dot_product)


# 📌 9. Finding Max, Min, and Sum
# Definition: Returns the highest, lowest, and sum of array elements.
# Usage: Used in statistics, financial calculations.
numbers = np.array([10, 20, 30, 40, 50])
print("⬆️ Max Value:", numbers.max())
print("⬇️ Min Value:", numbers.min())
print("➕ Sum of Values:", numbers.sum())


# 📌 10. Finding Mean, Median, and Standard Deviation
# Definition: NumPy provides statistical functions for analysis.
# Usage: Used in data science, analytics, and AI.
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("📊 Mean:", np.mean(data))
print("📏 Median:", np.median(data))
print("📉 Standard Deviation:", np.std(data))


# 📌 11. Filtering Elements with Conditions
# Definition: Selects elements based on conditions.
# Usage: Used in data filtering, AI feature selection.
filtered = data[data > 5]
print("🔍 Filtered (Greater than 5):", filtered)


# 📌 12. Stacking Arrays (Vertical and Horizontal)
# Definition: Combines multiple arrays along different axes.
# Usage: Used in data preprocessing and matrix operations.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
vert_stack = np.vstack((arr1, arr2))
hor_stack = np.hstack((arr1, arr2))
print("⬆️ Vertically Stacked:\n", vert_stack)
print("➡️ Horizontally Stacked:\n", hor_stack)


# 📌 13. Splitting Arrays
# Definition: Splits an array into multiple sub-arrays.
# Usage: Used in dividing datasets for training and testing in ML.
split_arr = np.array([1, 2, 3, 4, 5, 6])
split_result = np.split(split_arr, 2)  # Split into 2 equal parts
print("✂️ Split Arrays:", split_result)


# 📌 14. Transposing and Reshaping Matrices
# Definition: Flips rows and columns of a matrix.
# Usage: Used in data transformations, computer vision.
matrix = np.array([[1, 2, 3], [4, 5, 6]])
transposed = matrix.T
print("🔄 Transposed Matrix:\n", transposed)


# 📌 15. Saving and Loading NumPy Arrays
# Definition: Saves NumPy arrays to files for later use.
# Usage: Used in ML models, storing processed data.
np.save("my_array.npy", arr)
loaded_arr = np.load("my_array.npy")
print("💾 Loaded Array:", loaded_arr)


# 📌 16. Generating Random Integers
# Definition: Creates an array with random integers.
# Usage: Used in simulations, randomized testing.
rand_ints = np.random.randint(1, 100, (3, 3))  # 3x3 matrix of random numbers
print("🎲 Random Integers:\n", rand_ints)


# 📌 17. Finding Unique Elements and Counts
# Definition: Finds unique values and their occurrences.
# Usage: Used in category analysis, duplicate detection.
unique_values, counts = np.unique([1, 2, 2, 3, 3, 3, 4], return_counts=True)
print("✨ Unique Values:", unique_values)
print("📊 Occurrences:", counts)


# 📌 18. Generating Linearly Spaced Values
# Definition: Creates evenly spaced numbers over a range.
# Usage: Used in plotting graphs, numerical analysis.
lin_space = np.linspace(0, 10, 5)  # 5 values between 0 and 10
print("📏 Linearly Spaced Values:", lin_space)


# 📌 19. Boolean Masking in NumPy Arrays
# Definition: Uses Boolean conditions to filter arrays.
# Usage: Used in anomaly detection, filtering noisy data.
mask = data % 2 == 0  # Select even numbers
filtered_data = data[mask]
print("🧐 Even Numbers:", filtered_data)


# 📌 20. Flattening a Multi-Dimensional Array
# Definition: Converts a matrix into a single-dimensional array.
# Usage: Used in reshaping datasets for ML.
multi_arr = np.array([[1, 2, 3], [4, 5, 6]])
flattened = multi_arr.flatten()
print("📉 Flattened Array:", flattened)
