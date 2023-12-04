from collections import defaultdict
import time

fname = "2023/day4/input.txt"

start_time = time.time()

numbers_per_card = defaultdict(dict)

with open(fname, "r") as f:
    for line in f.readlines():
        card, data = line.split(": ")
        card_id = int(card.replace("Card", ""))
        data_winning, data_numbers = data.strip("\n").split("|")
        winning = [int(n) for n in data_winning.split(" ") if n != ""]
        numbers = [int(n) for n in data_numbers.split(" ") if n != ""]
        numbers_per_card[card_id] = {"winning": winning, "numbers": numbers}


print(f"processing input: {time.time() - start_time} s")
print()
time1 = time.time()

result1 = 0

for card_id, data in numbers_per_card.items():
    count = 0
    count_winning = 0
    for n in data["numbers"]:
        if n in data["winning"]:
            count = max(1, count*2)
            count_winning += 1
    numbers_per_card[card_id]["count"] = count_winning
    result1 += count

print("part 1: ", result1)
print(f"part 1: {time.time() - time1} s")
print()

# part 2
time2 = time.time()

result2 = 0
    
def process(cards, card_id):
    # find number of winning numbers
    count = cards[card_id]["count"]
    
    # stopping condition
    if count == 0:
        return 0
    else:
        return count + sum([process(cards, card_id + i) for i in range (1, count+1)])

for card_id in numbers_per_card.keys():
    result2 += process(numbers_per_card, card_id) + 1

print("part 2: ", result2)
print(f"part 2: {time.time() - time2} s")