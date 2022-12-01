with open("day1.txt", "r") as f:
    data = f.read().splitlines()

sum_calories = 0
elfs_total_calories = []
for line in data:
    if line == "":
        elfs_total_calories.append(sum_calories)
        sum_calories = 0
    else:
        sum_calories += int(line)

print(sum(sorted(elfs_total_calories, reverse=True)[0:3]))
