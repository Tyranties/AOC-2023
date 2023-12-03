import re

DIGIT_VALUES = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
}

with open("day1.txt", "r") as file:
    data = file.read()
    data = data.split("\n")

total = 0

for line in data:
    numbers = []

    spelled_numbers_pos = {}
    for digit in DIGIT_VALUES:
        spelled_numbers_pos[digit] = [m.start()
                                      for m in re.finditer(digit, line)]

    for i, char in enumerate(line):
        if char.isnumeric():
            numbers.append(int(char))
        else:
            for digit, positions in spelled_numbers_pos.items():
                if i in positions:
                    numbers.append(DIGIT_VALUES[digit])

    total += int(str(numbers[0]) + str(numbers[-1]))

print(total)
