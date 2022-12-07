with open("input.txt") as file:
    line = file.read()
    
#line = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
   
##### Part 1 #####
for itr in range(len(line)):
    if len(set(line[itr:itr+4])) >= 4:
        print("Part 1:", itr + 4)
        break
        
        
        
##### Part 2 #####
for itr in range(len(line)):
    if len(set(line[itr:itr+14])) >= 14:
        print("Part 2:", itr + 14)
        break