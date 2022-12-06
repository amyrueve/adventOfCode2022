import re

with open("./input.txt") as file:
	original_lines = file.read().splitlines()


original_stacks = [['Z', 'N'],
	['M', 'C', 'D'],
	['P']]
original_lines = ["move 1 from 2 to 1",
"move 3 from 1 to 3",
"move 2 from 2 to 1",
"move 1 from 1 to 2"]
'''

original_stacks = [['S', 'Z', 'P', 'D', 'L', 'B', 'F', 'C'], 
	['N', 'V', 'G', 'P', 'H', 'W', 'B'], 
	['F', 'W', 'B', 'J', 'G'], 
	['G', 'J', 'N', 'F', 'L', 'W', 'C', 'S'], 
	['W', 'J', 'L', 'T', 'P', 'M', 'S', 'H'], 
	['B', 'C', 'W', 'G', 'F', 'S'], 
	['H', 'T', 'P', 'M', 'Q', 'B', 'W'], 
	['F', 'S', 'W', 'T'], 
	['N', 'C', 'R']]
'''

##### Part 1 #####
lines = original_lines.copy()
stacks = original_stacks.copy()
for line in lines:
	#print(line)
	line  = line.replace("move ", "").replace(" from ", ",").replace(" to ", ",")
	line = line.split(",")
	
	num_to_move = int(line[0])
	old_stack_id = int(line[1]) - 1
	new_stack_id = int(line[2]) - 1
	
	
	for itr in range(num_to_move):
		stacks[new_stack_id].append(stacks[old_stack_id][-1])
		stacks[old_stack_id].pop()
		#print(stacks)
tops = ""
for itr in range(len(stacks)):
	tops += stacks[itr][-1]
print("Part 1:", tops )






with open("./input.txt") as file:
	original_lines = file.read().splitlines()
'''
original_stacks = [['Z', 'N'],
	['M', 'C', 'D'],
	['P']]
original_lines = ["move 1 from 2 to 1",
"move 3 from 1 to 3",
"move 2 from 2 to 1",
"move 1 from 1 to 2"]
'''

original_stacks = [['S', 'Z', 'P', 'D', 'L', 'B', 'F', 'C'], 
	['N', 'V', 'G', 'P', 'H', 'W', 'B'], 
	['F', 'W', 'B', 'J', 'G'], 
	['G', 'J', 'N', 'F', 'L', 'W', 'C', 'S'], 
	['W', 'J', 'L', 'T', 'P', 'M', 'S', 'H'], 
	['B', 'C', 'W', 'G', 'F', 'S'], 
	['H', 'T', 'P', 'M', 'Q', 'B', 'W'], 
	['F', 'S', 'W', 'T'], 
	['N', 'C', 'R']]

##### Part 2 #####
lines = original_lines.copy()
stacks = []
stacks = original_stacks.copy()
print('HERE')
print(stacks)
for line in lines:
	line  = line.replace("move ", "").replace(" from ", ",").replace(" to ", ",")
	line = line.split(",")

	num_to_move = int(line[0])
	old_stack_id = int(line[1]) - 1
	new_stack_id = int(line[2]) - 1

	print(stacks)
	
	stacks[new_stack_id] = stacks[new_stack_id] + stacks[old_stack_id][-num_to_move:]
	stacks[old_stack_id] = stacks[old_stack_id][:-num_to_move]

tops = ""
for itr in range(len(stacks)):
	tops += stacks[itr][-1]
print("Part 2:", tops)
