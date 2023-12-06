with open("day_06.txt", "r") as file:
    data = file.read()
    data = data.split("\n")

time = None
distance_record = None

for i, line in enumerate(data):
    line = int("".join(line.split()[1:]))
    if i == 0:
        time = line
    else:
        distance_record = line

left = 1

for speed in range(left, time + 1):
    distance = (time - speed) * speed
    if distance > distance_record:
        left = speed
        break

right = time - left
ans = right - left + 1
print(ans)
