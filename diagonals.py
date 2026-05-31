row_input = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(row_input)]

primary_diagonal = []
reverse_diagonal = []

for i in range(len(matrix)):
    primary_diagonal.append(matrix[i][i])
print(f'Primary diagonal: {", ".join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}')

for j in range(len(matrix)):
    reverse_diagonal.append(matrix[j][len(matrix)-1-j])
print(f'Secondary diagonal: {", ".join(str(x) for x in reverse_diagonal)}. Sum: {sum(reverse_diagonal)}')