num = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(num)]
result = 0

for i in range(len(matrix)):
    result += matrix[i][i]
print(result)
