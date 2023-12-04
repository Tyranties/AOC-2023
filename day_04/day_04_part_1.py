with open("day_04.txt", "r") as file:
    data = file.read()
    data = data.split("\n")

ans = 0

for line in data:
    line = line[9:].strip().split('|')
    winning = [int(num) for num in line[0].split()]
    entered = [int(num) for num in line[1].split()]
    card_points = 0
    match = 0
    for num in entered:
        if num in winning:
            match += 1
            if match == 1:
                card_points = 1
            else:
                card_points *= 2
    ans += card_points

print(ans)
