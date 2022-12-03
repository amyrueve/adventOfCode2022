with open('input.txt') as f:
    lines = f.readlines()
	
##### Part 1 #####

max_cals = 0
single_elf_accum = 0

for line in lines:
    try:
        single_elf_accum += int(line)
    except:
        max_cals = max_cals if single_elf_accum <= max_cals else single_elf_accum
        single_elf_accum = 0

print("part 1:", max_cals)


##### Part 2 #####

max_cals = [0, 0, 0]
single_elf_accum = 0

for line in lines:
    try:
        single_elf_accum += int(line)
    except:
        # max_cals = max_cals if single_elf_accum <= max_cals else single_elf_accum
        if min(max_cals) < single_elf_accum:
            max_cals.remove(min(max_cals))
            max_cals.append(single_elf_accum)
        single_elf_accum = 0

print("part 2:", sum(max_cals))