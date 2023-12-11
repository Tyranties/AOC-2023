with open("day_10.txt", "r") as file:
    grid = [list(line) for line in file.read().split("\n")]

for row in range(len(grid)):
    for column in range(len(grid[row])):
        if grid[row][column] == 'S':
            starting_row = row
            starting_column = column
            break
    else:
        continue
    break

check_pipes = [(starting_row, starting_column)]
seen_pipes = {(starting_row, starting_column)}

while len(check_pipes) > 0:
    row, column = check_pipes.pop(0)
    current_pipe = grid[row][column]

    if row > 0 and current_pipe in "S|LJ" and grid[row - 1][column] in "|7F" and (row - 1, column) not in seen_pipes:
        seen_pipes.add((row - 1, column))
        check_pipes.append((row - 1, column))

    if row < len(grid) - 1 and current_pipe in "S|7F" and grid[row + 1][column] in "|LJ" and (row + 1, column) not in seen_pipes:
        seen_pipes.add((row + 1, column))
        check_pipes.append((row + 1, column))

    if column > 0 and current_pipe in "S-7J" and grid[row][column - 1] in "-LF" and (row, column - 1) not in seen_pipes:
        seen_pipes.add((row, column - 1))
        check_pipes.append((row, column - 1))

    if column < len(grid[row]) - 1 and current_pipe in "S-LF" and grid[row][column + 1] in "-J7" and (row, column + 1) not in seen_pipes:
        seen_pipes.add((row, column + 1))
        check_pipes.append((row, column + 1))

furthest_distance = len(seen_pipes) // 2
print(furthest_distance)
