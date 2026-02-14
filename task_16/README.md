import numpy as np
import time

print("===== NUMPY TASK 16 =====")

# 1D Array
arr1 = np.array([1, 2, 3, 4])
print("\n1D Array:", arr1)

# 2D Array
arr2 = np.array([[1, 2], [3, 4]])
print("\n2D Array:\n", arr2)

# 3D Array
arr3 = np.array([[[1, 2], [3, 4]]])
print("\n3D Array:\n", arr3)

# Mathematical Operations
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("\nAddition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Broadcasting
arr = np.array([1, 2, 3])
print("\nBroadcasting (arr + 5):", arr + 5)

# Statistical Functions
data = np.array([10, 20, 30, 40, 50])
print("\nMean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Sum:", np.sum(data))
print("Max:", np.max(data))
print("Min:", np.min(data))

# NumPy vs Python List Speed Comparison
list1 = list(range(1000000))
start = time.time()
list2 = [x * 2 for x in list1]
print("\nPython List Time:", time.time() - start)

arr_np = np.arange(1000000)
start = time.time()
arr_np2 = arr_np * 2
print("NumPy Array Time:", time.time() - start)

# Random Data Generation
random_data = np.random.rand(3, 3)
print("\nRandom 3x3 Data:\n", random_data)

# Array Structure Information
print("\nShape of arr2:", arr2.shape)
print("Dimensions of arr2:", arr2.ndim)
print("Data Type of arr2:", arr2.dtype)

print("\n===== TASK COMPLETED SUCCESSFULLY =====")
