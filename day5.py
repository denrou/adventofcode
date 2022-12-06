import re
import copy

with open("day5.txt", "r") as f:
    data = f.read().splitlines()

load = []
for i, line in enumerate(data):
    if line == "":
        break
    for j, char in enumerate(line):
        if j % 4 == 1:
            if j // 4 >= len(load):
                load.append("")
            load[j // 4] += char
load = [list(string[:-1].strip()) for string in load]
load_copy = copy.deepcopy(load)

# Part 1
for line in data[len(load) + 1 :]:
    m, f, t = re.findall(r"\d+", line)
    m, f, t = int(m), int(f), int(t)
    for i in range(m):
        load[t - 1].insert(0, load[f - 1].pop(0))

print("".join([l[0] for l in load]))


# Part 2
load = load_copy
for line in data[len(load) + 1 :]:
    m, f, t = re.findall(r"\d+", line)
    m, f, t = int(m), int(f), int(t)
    for i in range(m):
        load[t - 1].insert(i, load[f - 1].pop(0))

print("".join([l[0] for l in load]))
