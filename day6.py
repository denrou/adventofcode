with open("day6.txt") as f:
    data = f.read()


def message(data, n=4):
    for i, _ in enumerate(data):
        if len(set(data[i : (i + n)])) == n:
            return i + n


print(message(data, 4))
print(message(data, 14))
