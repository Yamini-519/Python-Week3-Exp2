import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Element at row 1, col 2:", arr[1, 2])
print("First row:", arr[0, :])
print("First column:", arr[:, 0])
print("Subarray (rows 1-2, cols 1-2):\n", arr[1:3, 1:3])
print("Sum of all elements:", arr.sum())
print("Sum of each column:", arr.sum(axis=0))
print("Sum of each row:", arr.sum(axis=1))
