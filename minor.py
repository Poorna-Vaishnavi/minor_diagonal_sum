def sum_minor_diagonal(matrix):
    n = len(matrix)
    diagonal_sum = 0

    for i in range(n):
        diagonal_sum += matrix[i][n - i - 1]

    return diagonal_sum


n = int(input("Enter the size of the matrix: "))
matrix = []
for i in range(n):
    row = list(map(int, input(f"Enter the elements of row {i+1}: ").split()))
    matrix.append(row)

result = sum_minor_diagonal(matrix)
print("Sum of minor diagonal elements:", result)
