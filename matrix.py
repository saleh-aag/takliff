import numpy as np
import time

# Create 1000x1000 matrix with random values
matrix = np.random.rand(1000, 1000)

# Row sum calculation and timing
start_row = time.perf_counter()
row_sums = np.sum(matrix, axis=1)
end_row = time.perf_counter()
row_time = end_row - start_row

# Column sum calculation and timing
start_col = time.perf_counter()
col_sums = np.sum(matrix, axis=0)
end_col = time.perf_counter()
col_time = end_col - start_col

print(f"Row sums time: {row_time:.6f} seconds")
print(f"Column sums time: {col_time:.6f} seconds")