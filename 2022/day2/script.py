shape_to_nr = {s: i+1 for i, s in enumerate(['A', 'B', 'C'])}
shape_to_nr.update({s: i+1 for i, s in enumerate(['X', 'Y', 'Z'])})

# def score(you, other):
#     win_indicator = shape_to_nr[you] % 3 - shape_to_nr[other] % 3
#     return win_indicator*3 + 3

def score(you, other):
    if(shape_to_nr[you] - shape_to_nr[other] in [-2, 1, 1]):
        return 6
    elif(shape_to_nr[you] - shape_to_nr[other] in [-1, -1, 2]):
        return 0
    else:
        return 3

a = []

with open("day2/input.txt", 'r') as f:
    for line in f.readlines():
        plays = line.split(" ")
        other = plays[0].strip()
        you = plays[1].strip()

        sc = score(you, other)
        pts =  shape_to_nr[you]

        a.append(sc  + pts)

        if(sc + pts == 11):
            print("score is 11")
            print(you, ", ", other)
            print(sc, " + ", shape_to_nr[you])
            print()

print(sum(a))

# part 2
b = []

get_win_response = {'A': 'B', 'B': 'C', 'C': 'A'}
get_lose_response = {'A': 'C', 'B': 'A', 'C': 'B'}


with open("day2/input.txt", 'r') as f:
    for line in f.readlines():
        plays = line.split(" ")
        other = plays[0].strip()
        outcome = plays[1].strip()

        if(outcome == 'X'):
            you = get_lose_response[other]
        elif(outcome == "Z"):
            you = get_win_response[other]
        else:
            you = other
        
        sc = score(you, other)
        pts = shape_to_nr[you]

        b.append(sc + pts)

print(sum(b))
        