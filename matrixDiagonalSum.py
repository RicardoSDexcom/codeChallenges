matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

mtx = [element for row in matrix for element in row]

import math

original_list = mtx

# Calculate the square root of the length of the original list
sqrt_length = int(math.sqrt(len(original_list)))

# Create n lists of length sqrt
sublists = [original_list[i:i+sqrt_length] for i in range(0, len(original_list), sqrt_length)]

print(sublists)
rows = len(matrix)
cols = len(matrix[0])
main_diagonal_sum = sum(matrix[i][i] for i in range(min(rows, cols)))
secondary_diagonal_sum = sum(matrix[i][cols - 1 - i] for i in range(min(rows, cols)))
print(main_diagonal_sum + secondary_diagonal_sum)
