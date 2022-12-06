priority = {k: i+1 for i, k in enumerate('abcdefghijklmnopqrstuvwxyz')}
priority.update({k: i+27 for i, k in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')})

mistakes = []

with open("day3/input.txt", 'r') as f:
	for line in f.readlines():
		line = line.strip('\n')
		length = len(line)
		half1 = line[:int(length/2)]
		half2 = line[int(length/2):]
		#print(length,len(half1), len(half2))
		m = set(half1).intersection(set(half2))
		#print(m)
		mistakes.append(list(m)[0])

mistakevalues = [priority[m] for m in mistakes]

print(sum(mistakevalues))



badges = []

with open("day3/input.txt", 'r') as f:
	for i, line in enumerate(f.readlines()):
		line = line.strip('\n')
		
		if(i % 3 == 0):
			if(i != 0):
				#print(i, badge)
				badges.append(list(badge)[0])
			badge = set(line)
		else:
			badge = badge.intersection(set(line))

	badges.append(list(badge)[0])
			
badgevalues = [priority[b] for b in badges]

print(sum(badgevalues))
