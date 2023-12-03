import re

result = 0
with open("2023/day1/input_simon.txt", "r") as f:
    for line in f.readlines():
        line = re.sub("[^0-9]", "", line)
        value = int(line[0] + line[-1])
        result += value

print("part 1: ", result)
print()

# PART 2
word_to_digit = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

result2 = 0

with open("2023/day1/input_simon.txt", "r") as f:
    for line in f.readlines():
        line = line.strip("\n")

        # look for words to replace with digits greedily
        resulting_line = ""
        j = 0
        for i in range(len(line) + 1):
            if i > j:
                for k in range(j, i):
                    if line[k:i] in word_to_digit.keys():
                        resulting_line += line[j:k]
                        resulting_line += str(word_to_digit[line[k:i]])
                        j = i
        resulting_line += line[j:None]

        resulting_line = re.sub("[^0-9]", "", resulting_line)
        value = int(resulting_line[0] + resulting_line[-1])
        result2 += value

print("part 2: ", result2)
