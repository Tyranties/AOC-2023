with open("day_06.txt", "r") as file:
    data = file.read()
    data = data.split("\n")

race_data = []

for i, line in enumerate(data):
    line = int("".join(line.split()[1:]))
    race_data.append(line)

left = None
for speed in range(1, race_data[0] + 1):
    distance = (race_data[0] - speed) * speed
    if distance > race_data[1]:
        left = speed
        break

right = race_data[0] - left
ans = right - left + 1
print(ans)
