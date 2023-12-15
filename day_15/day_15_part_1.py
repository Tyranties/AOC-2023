with open("day_15.txt", "r") as file:
    steps = file.read().split(",")

sum_results = 0
for step in steps:
    current_value = 0
    for char in step:
        ascii_value = ord(char)
        current_value += ascii_value
        current_value *= 17
        current_value %= 256
    sum_results += current_value

print(sum_results)
