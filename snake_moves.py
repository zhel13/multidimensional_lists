from collections import deque

row, col = map(int, input().split())

sentence = input()
result = deque(sentence)
matrix = []
for i in range(row):
    matrix.append([])
    for j in range(col):
        ch = result.popleft()
        matrix[i].append(ch)
        result.append(ch)

for i in range(len(matrix)):
    if i % 2 != 0:
        matrix[i] = matrix[i][::-1]
    print(''.join(matrix[i]))



