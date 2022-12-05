import re

with open("input.txt") as file:
	lines = file.read().splitlines()

#lines = ['2-4,6-8','2-3,4-5','5-7,7-9','2-8,3-7','6-6,4-6','2-6,4-8']
##### Part 1 #####
accum = 0

for line in lines:
	line = re.split("-|,|-", line)
	if (int(line[0]) <= int(line[2])) & (int(line[3]) <= int(line[1])):
		accum += 1
	elif (int(line[2]) <= int(line[0])) & (int(line[1]) <= int(line[3])):
		accum += 1

print('Part 1', accum)


##### Part 2 #####
accum = 0

for line in lines:
	line = re.split("-|,|-", line)
	if (int(line[0]) <= int(line[2])) & (int(line[2]) <= int(line[1])):
		accum += 1
	elif (int(line[2]) <= int(line[0])) & (int(line[0]) <= int(line[3])):
		accum += 1

print('Part 2:', accum)
