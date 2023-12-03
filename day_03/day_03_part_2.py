SYMBOL = "*"

with open("day_03.txt", "r") as file:
    data = file.read()
    data = data.split("\n")

grid = []
ans = 0

for line in data:
    grid.append(list(line))

gears = {}

for i, row in enumerate(grid):
    index = 0
    while index < len(row):
        if row[index].isnumeric():
            positions = []
            num = row[index]
            positions.append(index)
            ended = False
            index += 1
            while not ended and index < len(row):
                if row[index].isnumeric():
                    num += row[index]
                    positions.append(index)
                    index += 1
                else:
                    ended = True

            num = int(num)
            adjacent_chars_pos = []

            if positions[0] != 0:  # left
                adjacent_chars_pos.append((i, positions[0] - 1))
            if positions[0] != 0 and i != 0:  # top left
                adjacent_chars_pos.append((i - 1, positions[0] - 1))
            if positions[-1] + 1 != len(row) and i != 0:  # top right
                adjacent_chars_pos.append((i - 1, positions[-1] + 1))
            if positions[-1] + 1 != len(row):  # right
                adjacent_chars_pos.append((i, positions[-1] + 1))
            if positions[-1] + 1 != len(row) and i + 1 != len(grid):  # bottom right
                adjacent_chars_pos.append((i + 1, positions[-1] + 1))
            if positions[0] != 0 and i + 1 != len(grid):  # bottom left
                adjacent_chars_pos.append((i + 1, positions[0] - 1))

            if len(positions) == 1:
                if i != 0:  # top
                    adjacent_chars_pos += [(i - 1, positions[0])]
                if i + 1 != len(grid):  # bottom
                    adjacent_chars_pos += [(i + 1, positions[0])]

            elif len(positions) == 2:
                if i != 0:  # top
                    adjacent_chars_pos += [(i - 1, positions[0]),
                                           (i - 1, positions[1])]
                if i + 1 != len(grid):  # bottom
                    adjacent_chars_pos += [(i + 1, positions[0]),
                                           (i + 1, positions[1])]

            elif len(positions) == 3:
                if i != 0:  # top
                    adjacent_chars_pos += [(i - 1, positions[0]),
                                           (i - 1, positions[1]),
                                           (i - 1, positions[2])]
                if i + 1 != len(grid):  # bottom
                    adjacent_chars_pos += [(i + 1, positions[0]),
                                           (i + 1, positions[1]),
                                           (i + 1, positions[2])]

            for pos in adjacent_chars_pos:
                if grid[pos[0]][pos[1]] == SYMBOL:
                    if pos in gears:
                        gears[pos] += [num]
                    else:
                        gears[pos] = [num]

        index += 1

for pos, nums in gears.items():
    if len(nums) == 2:
        gear_ratio = nums[0] * nums[1]
        ans += gear_ratio

print(ans)
