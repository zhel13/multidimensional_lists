row, col = [int(x) for x in input().split()]

matrix = [[char for char in input().split()] for _ in range(row)]
counter = 0

for i in range(row-1):
    for j in range(col-1):
        first_char = matrix[i][j]
        second_char = matrix[i][j+1]
        third_char = matrix[i+1][j]
        fourth_char = matrix[i+1][j+1]
        if first_char == second_char and first_char == third_char and first_char == fourth_char:
            counter += 1
print(counter)
