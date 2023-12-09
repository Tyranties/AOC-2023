histories = []

with open("day_09.txt", "r") as file:
    data = file.read().split("\n")
    for line in data:
        histories.append(list(map(int, line.split())))

extrapolated_values = []

for history in histories:
    sublists = [history]
    all_zeroes = False
    while not all_zeroes:
        sublist = []
        for i in range(len(sublists[-1]) - 1):
            difference = sublists[-1][i + 1] - sublists[-1][i]
            sublist.append(difference)
        all_zeroes = all(element == 0 for element in sublist)
        sublists.append(sublist)

    sublists[-1].insert(0, 0)
    for i in range(len(sublists) - 2, -1, -1):
        extrapolated_value = sublists[i][0] - sublists[i + 1][0]
        sublists[i].insert(0, extrapolated_value)

    extrapolated_values.append(sublists[0][0])

ans = sum(extrapolated_values)
print(ans)
