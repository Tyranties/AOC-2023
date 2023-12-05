import re

with open("day_04.txt", "r") as file:
    data = file.read()
    data = data.split("\n")

scratchcard_dict = {i: 1 for i in range(1, 219)}

for current_num, line in enumerate(data):
    line = re.split(r'\||:', line)
    card_num = int(line[0].split()[1])
    winning = [int(num) for num in line[1].split()]
    entered = [int(num) for num in line[2].split()]
    match = 0
    for num in entered:
        if num in winning:
            match += 1

    for i in range(1, match + 1):
        scratchcard_dict[card_num + i] += scratchcard_dict[card_num]

ans = sum(scratchcard_dict.values())
print(ans)
