row, col = map(int, input().split())

matrix = []

for i in range(row):
    matrix.append([])
    for j in range(col):
        matrix[i].append(chr(97+i) + chr(97+j+i) + chr(97+i))

for k in range(len(matrix)):
    print(*matrix[k])
