# part 1
with open("day6/input.txt", 'r') as f:
    line = f.readlines()[0].strip("\n")    
    for i, c in enumerate(line[3:]):
        last_four = line[i:i+4]
        if(len(set(last_four)) == 4):
            print(i + 4)
            break

# part 2
with open("day6/input.txt", 'r') as f:
    line = f.readlines()[0].strip("\n")    
    for i, c in enumerate(line[13:]):
        last_four = line[i:i+14]
        if(len(set(last_four)) == 14):
            print(i + 14)
            break