import math

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

a = -1
b = time
c = -distance_record

x_1 = int((-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
x_2 = int((-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))

ans = abs(x_1 - x_2)

print(ans)
