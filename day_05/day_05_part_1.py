from itertools import groupby

with open("day_05_test.txt", "r") as file:
    data = file.read()
    data = data.split("\n")

almanac_sections = [list(group) for key, group in groupby(
    data, key=lambda x: x == "") if not key]

seeds = []
mappings_list = [{} for _ in range(7)]

for i, almanac_section in enumerate(almanac_sections):
    if i == 0:
        almanac_section = almanac_section[0].split()
        for item in almanac_section[1:]:
            seeds.append(int(item))
        continue

    almanac_section = almanac_section[1:]

    for mapping in almanac_section:
        numbers = mapping.split()
        destination_start = int(numbers[0])
        source_range = (int(numbers[1]), int(numbers[1]) + int(numbers[2]))

        mappings_list[i - 1][source_range] = destination_start

for i in range(7):
    current_mappping = mappings_list[i]
    for i, x in enumerate(seeds):
        found = False
        for source, destination in current_mappping.items():
            if x in range(source[0], source[1] + 1):
                difference = x - source[0]
                new_val = destination + difference
                found = True
                break
        if not found:
            new_val = x

        seeds[i] = new_val

ans = min(seeds)
print(ans)
