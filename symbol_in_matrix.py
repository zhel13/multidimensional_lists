rows = int(input())

matrix = []

for i in range(rows):
    characters = list(input())
    matrix.append(characters)

search_symbol = input()
position = None
is_found = False

for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == search_symbol:
            position = (row, col)
            is_found = True
            print(position)
            exit()

if not is_found:
    print(f"{search_symbol} does not occur in the matrix")