with open("day_15.txt", "r") as file:
    steps = file.read().split(",")

boxes = {i: {} for i in range(256)}

for step in steps:
    index_equal = step.find('=')
    index_minus = step.find('-')
    index = min(index_equal, index_minus) if index_equal != - \
        1 and index_minus != -1 else max(index_equal, index_minus)

    label = step[:index]

    current_value = 0
    for char in label:
        ascii_value = ord(char)
        current_value += ascii_value
        current_value *= 17
        current_value %= 256

    if index_equal == -1:  # minus
        if label in boxes[current_value]:
            boxes[current_value].pop(label)

    if index_minus == -1:  # equal
        value = int(step[index + 1:])
        if label in boxes[current_value]:
            boxes[current_value][label] = value
        if label not in boxes[current_value]:
            boxes[current_value][label] = value

total_focusing_power = 0
for label, lens in boxes.items():
    if lens:
        for i, (string, focal_length) in enumerate(lens.items()):
            total_focusing_power += (label + 1) * (i + 1) * focal_length

print(total_focusing_power)
