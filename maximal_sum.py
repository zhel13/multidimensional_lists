row, col = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(row)]
maximum_sum = float('-inf')
sub_matrix = [[], [], []]
total_sum = 0

for i in range(row-2):
    for j in range(col-2):
        first_row = [x for x in matrix[i][j:j+3]]
        second_row = [x for x in matrix[i+1][j:j+3]]
        third_row = [x for x in matrix[i+2][j:j+3]]
        total_sum = sum(first_row) + sum(second_row) + sum(third_row)
        if total_sum > maximum_sum:
            maximum_sum = total_sum
            sub_matrix[0] = first_row
            sub_matrix[1] = second_row
            sub_matrix[2] = third_row

print(f"Sum = {maximum_sum}")
for i in sub_matrix:
    print(*i)
