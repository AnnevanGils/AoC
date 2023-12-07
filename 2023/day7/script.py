import numpy as np
from collections import defaultdict
import itertools

fname = "2023/day7/input.txt"

hand_order = {
    k: i
    for i, k in enumerate(["5", "4_1", "3_2", "3_1_1", "2_2_1", "2_1_1_1", "1_1_1_1_1"])
}

card_to_letter = {c: l for c, l in zip("AKQJT98765432", "abcdefghijklm")}


def get_hand_mapping(card):
    return "_".join(
        [str(i) for i in np.sort(np.unique(list(card), return_counts=True)[1])[::-1]]
    )


data1 = defaultdict(lambda: {"cards": [], "bids": []})

with open(fname, "r") as f:
    for line in f.read().split("\n"):
        card, bid = line.split(" ")
        hand = get_hand_mapping(card)
        data1[hand]["cards"].append("".join([card_to_letter[c] for c in card]))
        data1[hand]["bids"].append(int(bid))

data1 = {h: {k: np.array(v) for k, v in l.items()} for h, l in data1.items()}

all_bids_ranked = []

for h in list(hand_order.keys())[::-1]:
    if h in data1:
        idx_sorted = np.argsort(data1[h]["cards"])
        all_bids_ranked.extend(data1[h]["bids"][idx_sorted].tolist()[::-1])

print("part 1:", sum([(i + 1) * b for i, b in enumerate(all_bids_ranked)]))
print()

# part 2
data2 = defaultdict(lambda: {"cards": [], "bids": []})

card_to_letter2 = {c: l for c, l in zip("AKQT98765432J", "abcdefghijklm")}

with open(fname, "r") as f:
    for line in f.read().split("\n"):
        card, bid = line.split(" ")
        hand = get_hand_mapping(card)

        if "J" in card:
            a = np.array(list(card))
            relevant_letters = "".join(set(card.replace("J", "")))
            j_idx = np.argwhere(a == "J").flatten()
            j_replacement_options = itertools.combinations_with_replacement(
                relevant_letters, len(j_idx)
            )

            for t in j_replacement_options:
                new_card = np.copy(a)
                new_card[j_idx] = t
                new_hand = get_hand_mapping("".join(new_card))
                if hand_order[new_hand] < hand_order[hand]:
                    hand = new_hand

        data2[hand]["cards"].append("".join([card_to_letter2[c] for c in card]))
        data2[hand]["bids"].append(int(bid))

data2 = {h: {k: np.array(v) for k, v in l.items()} for h, l in data2.items()}

all_bids_ranked = []
for h in list(hand_order.keys())[::-1]:
    if h in data2:
        idx_sorted = np.argsort(data2[h]["cards"])
        all_bids_ranked.extend(data2[h]["bids"][idx_sorted].tolist()[::-1])


print("part 2:", sum([(i + 1) * b for i, b in enumerate(all_bids_ranked)]))
