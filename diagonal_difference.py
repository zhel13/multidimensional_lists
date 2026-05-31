row_input = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(row_input)]
primary_diagonal = [matrix[i][i] for i in range(len(matrix))]
secondary_diagonal = [matrix[j][len(matrix)-1-j] for j in range(len(matrix))]

difference = sum(primary_diagonal) - sum(secondary_diagonal)
print(abs(difference))