with open("input.txt") as file:
    lines = file.read().splitlines()
    
    
#lines = ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg', 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']
    
##### Part 1 #####
accum = 0

for line in lines:
    #Convert lines to two lists of objects with equal numbers 
    objs = list(line)
    num_objs = len(objs) #0 indexing
    half_idx = int(num_objs / 2)
    compartment_1 = objs[:half_idx]
    compartment_2 = objs[half_idx:]
    
    #Set subtraction to find overlap
    in_both = list(set(compartment_1) & set(compartment_2))
    for obj in in_both:
        obj_unicode = ord(obj)
        obj_val = obj_unicode - 38 if obj_unicode < 95 else obj_unicode - 96
        accum += obj_val
    
print('Part 1:', accum)


##### Part 2 #####
accum = 0

for itr in range(0, len(lines), 3):
    sack_1 = lines[itr]
    sack_2 = lines[itr + 1]
    sack_3 = lines[itr + 2]
    in_all_three = list(set(sack_1) & set(sack_2) & set(sack_3))
    
    for obj in in_all_three:
        obj_unicode = ord(obj)
        obj_val = obj_unicode - 38 if obj_unicode < 95 else obj_unicode - 96
        accum += obj_val
        
print('Part 2:', accum)