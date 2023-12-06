with open("day_06.txt", "r") as file:
    data = file.read()
    data = data.split("\n")

races = []

for line in data:
    line = list(map(int, line.split()[1:]))
    if len(races) == 0:
        line = [[num] for num in line]
        races += line
    else:
        for i, time in enumerate(line):
            races[i].append(time)

ans = 1

for race in races:
    record_breakers = 0
    for speed in range(1, race[0]):
        distance = (race[0] - speed) * speed
        if distance > race[1]:
            record_breakers += 1
    ans *= (record_breakers)

print(ans)
