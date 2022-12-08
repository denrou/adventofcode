with open("day8.txt") as f:
    left_right = [[int(i) for i in list(l)] for l in f.read().splitlines()]

right_left = [l[::-1] for l in left_right[::-1]]
up_down = [list(l[::-1]) for l in zip(*left_right)]
down_up = [list(l[::-1]) for l in zip(*right_left)]

data = [left_right, up_down, right_left, down_up]
mask = [[0] * len(data[0][0]) for _ in range(len(data[0]))]

# Part 1

for i, m in enumerate(data):
    for j in range(len(m)):
        max_val = -1
        for k in range(len(m[0])):
            if i == 0:
                row_index = j
                col_index = k
            elif i == 1:
                row_index = len(m[0]) - 1 - k
                col_index = j
            elif i == 2:
                row_index = len(m[0]) - 1 - j
                col_index = len(m[0]) - 1 - k
            elif i == 3:
                row_index = k
                col_index = len(m[0]) - 1 - j
            if m[j][k] > max_val:
                max_val = m[j][k]
                mask[row_index][col_index] = 1


print(sum([sum(l) for l in mask]))

# Part 2

mask = [[1] * len(data[0][0]) for _ in range(len(data[0]))]
for i, m in enumerate(data):
    mask_tmp = [[0] * len(data[0][0]) for _ in range(len(data[0]))]
    for j in range(len(m)):
        for k in range(len(m[0])):
            if i == 0:
                row_index = j
                col_index = k
            elif i == 1:
                row_index = len(m[0]) - 1 - k
                col_index = j
            elif i == 2:
                row_index = len(m[0]) - 1 - j
                col_index = len(m[0]) - 1 - k
            elif i == 3:
                row_index = k
                col_index = len(m[0]) - 1 - j
            tmp_k = k
            while tmp_k < len(m[j]) - 1:
                mask_tmp[row_index][col_index] += 1
                if m[j][k] <= m[j][tmp_k + 1]:
                    break
                tmp_k += 1

    for j in range(len(m)):
        for k in range(len(m[0])):
            mask[j][k] *= mask_tmp[j][k]

print(max([max(l) for l in mask]))
