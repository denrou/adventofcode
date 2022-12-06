with open("day4.txt", "r") as f:
    data = f.read().splitlines()

# Part 1
count = 0
for line in data:
    groups = line.split(",")
    start_pair_1, end_pair_1 = groups[0].split("-")
    start_pair_2, end_pair_2 = groups[1].split("-")
    if (
        int(start_pair_1) <= int(start_pair_2) and int(end_pair_1) >= int(end_pair_2)
    ) or (
        int(start_pair_1) >= int(start_pair_2) and int(end_pair_1) <= int(end_pair_2)
    ):
        count += 1

print(count)

# Part 2
count = 0
for line in data:
    groups = line.split(",")
    start_pair_1, end_pair_1 = groups[0].split("-")
    start_pair_2, end_pair_2 = groups[1].split("-")
    if (
        int(start_pair_1) <= int(end_pair_2) and int(end_pair_1) >= int(start_pair_2)
    ) or (int(start_pair_1) >= int(end_pair_2) and int(end_pair_1) <= int(end_pair_2)):
        count += 1

print(count)
