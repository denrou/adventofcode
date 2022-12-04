with open("day3.txt", "r") as f:
    data = f.readlines()

weight = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
}

# Part 1
score = 0
for ruckstack in data:
    half = len(ruckstack) // 2
    compartment_1 = set(ruckstack[0:half])
    compartment_2 = set(ruckstack[half : len(ruckstack)])
    wrong = compartment_1.intersection(compartment_2)
    score += weight[wrong.pop()]

print(score)

# Part 2
score = 0
for i, ruckstack in enumerate(data):
    if i % 3 == 0:
        score_group = 0
        set_group = set(ruckstack)
    else:
        set_group = set_group.intersection(set(ruckstack))
        if i % 3 == 2:
            set_group.remove("\n")
            score += weight[set_group.pop()]

print(score)
