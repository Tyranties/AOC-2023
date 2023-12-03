import re

with open("day_02.txt", "r") as file:
    data = file.read()
    data = data.split("\n")

ans = 0

for line in data:
    line = re.split(';|:', line)
    line_list = []
    for i, part in enumerate(line):
        if i == 0:
            line_list.append([int(line[0].split()[1])])
        else:
            cubes_dict = {}
            part = part.strip().split(',')
            for cubes in part:
                cubes = cubes.split()
                cubes_dict[cubes[1]] = int(cubes[0])
            line_list.append(cubes_dict)

    min_cubes = {}

    for game in line_list[1:]:
        for colour, amount in game.items():
            min_cubes.setdefault(colour, amount)
            min_cubes[colour] = max(min_cubes[colour], amount)

    power_set = 1
    for min_cubes in min_cubes.values():
        power_set *= min_cubes

    ans += power_set


print(ans)
