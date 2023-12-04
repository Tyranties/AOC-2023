import re

with open("day_04.txt", "r") as file:
    data = file.read()
    data = data.split("\n")

scratchcard_dict = {}

for current_num, line in enumerate(data):
    line = re.split(r'\||:', line)
    card_num = int(line[0].split()[1])
    winning = [int(num) for num in line[1].split()]
    entered = [int(num) for num in line[2].split()]
    match = 0
    for num in entered:
        if num in winning:
            match += 1

    if card_num not in scratchcard_dict:
        scratchcard_dict[card_num] = 1

    for i in range(scratchcard_dict[card_num]):
        for j in range(1, match + 1):
            if card_num + j not in scratchcard_dict:
                scratchcard_dict[card_num + j] = 2
            else:
                scratchcard_dict[card_num + j] += 1

ans = sum(scratchcard_dict.values())
print(ans)
