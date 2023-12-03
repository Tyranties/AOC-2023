with open("day1.txt", "r") as file:
    data = file.read()
    data = data.split("\n")

total = 0

for line in data:
    numbers = [int(char) for char in line if char.isdigit()]
    if len(numbers) == 1:
        number = int(str(numbers[0]) + str(numbers[0]))
    else:
        number = int(str(numbers[0]) + str(numbers[-1]))
    total += number

print(total)
