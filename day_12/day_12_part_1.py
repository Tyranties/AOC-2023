cache = {}


def count_combinations(springs, damaged_nums):
    if len(springs) == 0:
        if damaged_nums == ():
            return 1
        return 0

    if damaged_nums == ():
        if "#" not in springs:
            return 1
        return 0

    total_combinations = 0

    if (springs, damaged_nums) in cache:
        return cache[(springs, damaged_nums)]

    if springs[0] in ".?":
        total_combinations += count_combinations(springs[1:], damaged_nums)

    if springs[0] in "#?":
        if damaged_nums[0] <= len(springs) and "." not in springs[:damaged_nums[0]] and (damaged_nums[0] == len(springs) or springs[damaged_nums[0]] != "#"):
            total_combinations += count_combinations(
                springs[damaged_nums[0] + 1:], damaged_nums[1:])

    cache[springs, damaged_nums] = total_combinations

    return total_combinations


with open("day_12.txt", "r") as file:
    springs_list = file.read().splitlines()

total_combinations = 0
for line in springs_list:
    springs, damaged_nums = line.split()
    damaged_nums = tuple(map(int, damaged_nums.split(",")))
    total_combinations += count_combinations(springs, damaged_nums)

print(total_combinations)
