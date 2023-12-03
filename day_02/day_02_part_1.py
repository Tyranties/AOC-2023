import re

MAXIMUM = {'red': 12, 'green': 13, 'blue': 14}

with open("day_02.txt", "r") as file:
    data = file.read()
    data = data.split("\n")

ans = 0

for line in data:
    line = re.split(';|:', line)
    line_list = []
    for i, part in enumerate(line):
        if i == 0:
            part = part.split()
            line_list.append(int(part[1]))
        else:
            cubes_dict = {}
            part = part.strip().split(',')
            for cubes in part:
                cubes = cubes.split()
                cubes_dict[cubes[1]] = int(cubes[0])
            line_list.append(cubes_dict)

    max_reached = False

    for game in line_list[1:]:
        for colour, amount in game.items():
            if amount > MAXIMUM[colour]:
                max_reached = True
                break

    if not max_reached:
        ans += line_list[0]


print(ans)
