with open("input.txt") as file:
    lines = file.readlines()
    
#lines = ['A Y', 'B X', 'C Z']    


##### Part 1 #####

#A and X are rock
#B and Y are paper
#C and Z are scissors

#Loss is 0, draw is 3, win is 6 points   

score_accum = 0

for line in lines:
    elf = line[0]
    me = line[2]

    match me:
        case 'X':
            score_accum += 1
            match elf:
                case 'A':
                    score_accum += 3
                case 'B':
                    score_accum += 0
                case 'C':
                    score_accum += 6
        case 'Y':
            score_accum += 2
            match elf:
                case 'A':
                    score_accum += 6
                case 'B':
                    score_accum += 3
                case 'C':
                    score_accum += 0
        case 'Z':
            score_accum += 3
            match elf:
                case 'A':
                    score_accum += 0
                case 'B':
                    score_accum += 6
                case 'C':
                    score_accum += 3
                    
print("part 1", score_accum)




##### Part 2 #####

#A, B, C are still rock, paper, scissors
#X is lose
#Y is draw
#Z is win

score_accum = 0

for line in lines:
    elf = line[0]
    me = line[2]

    match me:
        case 'X':
            score_accum += 0
            match elf:
                case 'A':
                    score_accum += 3
                case 'B':
                    score_accum += 1
                case 'C':
                    score_accum += 2
        case 'Y':
            score_accum += 3
            match elf:
                case 'A':
                    score_accum += 1
                case 'B':
                    score_accum += 2
                case 'C':
                    score_accum += 3
        case 'Z':
            score_accum += 6
            match elf:
                case 'A':
                    score_accum += 2
                case 'B':
                    score_accum += 3
                case 'C':
                    score_accum += 1
                    
print("part 2", score_accum)
    
