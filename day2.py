with open("day2.txt", "r") as f:
    data = f.read().splitlines()

score_dict_part_1 = {
    "B X": 1,
    "C Y": 2,
    "A Z": 3,
    "A X": 4,
    "B Y": 5,
    "C Z": 6,
    "C X": 7,
    "A Y": 8,
    "B Z": 9,
}

score_dict_part_2 = {
    "B X": 1,
    "C X": 2,
    "A X": 3,
    "A Y": 4,
    "B Y": 5,
    "C Y": 6,
    "C Z": 7,
    "A Z": 8,
    "B Z": 9,
}

score = 0

for line in data:
    score += score_dict_part_2[line]

print(score)
