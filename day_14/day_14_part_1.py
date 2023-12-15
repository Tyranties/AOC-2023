with open("day_14.txt", "r") as file:
    platform = file.read().splitlines()

platform = [list(row[::-1]) for row in zip(*platform)]

for row in platform:
    for i, char in reversed(list(enumerate(row))):
        if char == "O":
            previous_index = i
            current_index = i
            reached_end = False
            while not reached_end:
                if current_index + 1 < len(row) and row[current_index + 1] not in "#O":
                    current_index += 1
                else:
                    reached_end = True
            row[previous_index] = "."
            row[current_index] = "O"

platform = [[platform[j][i] for j in range(
    len(platform))] for i in range(len(platform[0])-1, -1, -1)]

north_wall_load = 0
current_row_num = len(platform)
for row in platform:
    for char in row:
        if char == "O":
            north_wall_load += current_row_num
    current_row_num -= 1

print(north_wall_load)
