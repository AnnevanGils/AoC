import re

count = 0

with open("day4/input.txt", 'r') as f:
	pattern = "(\d+)\-(\d+)\,(\d+)\-(\d+)"
	lines = f.readlines()
	for line in lines:
		g = re.match(pattern, line.strip("\n")).groups()
		if(int(g[0])<=int(g[2]) and int(g[1])>=int(g[3])):
				count += 1
		elif(int(g[2])<=int(g[0]) and int(g[3])>=int(g[1])):
				count += 1

print(count)

# part 2
count = 0

with open("day4/input.txt", 'r') as f:
	pattern = "(\d+)\-(\d+)\,(\d+)\-(\d+)"
	lines = f.readlines()
	for line in lines:
		g = re.match(pattern, line.strip("\n")).groups()
		if(int(g[0])<=int(g[2]) and int(g[1])>=int(g[2])):
			count += 1
		elif(int(g[0])<=int(g[2]) and int(g[1])>=int(g[3])):
				count += 1
		elif(int(g[2])<=int(g[0]) and int(g[3])>=int(g[0])):
				count += 1
		elif(int(g[2])<=int(g[0]) and int(g[3])>=int(g[1])):
				count += 1

print(count)