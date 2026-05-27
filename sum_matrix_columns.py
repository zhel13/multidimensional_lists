row, col = [int(x) for x in input().split(', ')]
matrix=[[int(x) for x in input().split()] for _ in range(row)]
total_column = 0

for i in range(col):
    for j in range(row):
        total_column += matrix[j][i]
    print(total_column)
    total_column = 0






