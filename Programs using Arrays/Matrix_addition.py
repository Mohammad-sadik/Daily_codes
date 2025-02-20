rows = int(input("Enter the row of the matrix: "))

matrix_a = [[int(i) for i in input("Enter 1st matrix: ").split()] for _ in range(rows)]
matrix_b = [[int(i) for i in input("Enter 2nd matrix: ").split()] for _ in range(rows)]
final_matrix = [[matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]
for row in final_matrix:
    print(row)