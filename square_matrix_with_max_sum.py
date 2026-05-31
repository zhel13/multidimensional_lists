row_count, col_count = [int(x) for x in input().split(', ')]

matrix = []
max_sum = float('-inf')
sub_matrix = []

for i in range(row_count):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

for row_index in range(row_count-1):
    for col_index in range(col_count-1):
        first_element = matrix[row_index][col_index]
        right_element = matrix[row_index][col_index+1]
        below_element = matrix[row_index+1][col_index]
        diagonal_element = matrix[row_index+1][col_index+1]
        total_sum = first_element + right_element + below_element + diagonal_element
        if total_sum > max_sum:
            max_sum = total_sum
            sub_matrix = [[first_element, right_element], [below_element, diagonal_element]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)



