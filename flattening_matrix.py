rows = int(input())
matrix =[[int(x) for x in input().split(', ')] for _ in range(rows)]
flattening = [x for row in matrix for x in row]
print(flattening)