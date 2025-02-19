row = int(input("Enter num of rows : "))
matrix = [input("Enter the matrix : ").split() for _ in range(row)]
transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print(f"Transpose matrix : {transpose}")