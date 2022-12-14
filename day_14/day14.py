import numpy as np

test = False

if test:
    lines = ["498,4 -> 498,6 -> 496,6", "503,4 -> 502,4 -> 502,9 -> 494,9"] 
    image = np.full((10,10), '.')
    drop_point = (0, 7)
else:
    with open('./input.txt') as file:
        lines = file.read().splitlines()
    image = np.full((600,600), '.')
    drop_point = (0, 500)



##### Part 1 #####
def draw(x1, y1, x2, y2, image):
    image[min(y1, y2):max(y1, y2)+1, min(x1, x2):max(x1, x2)+1] = '#'
    return image

# Draws the walls of image
for line in lines:
    line  = line.replace(" -> ", ",")
    line = line.split(",")
    x_list = []
    y_list = []
    num_pairs = int(len(line) / 2)
    for itr in range(0, num_pairs * 2, 2):
        if test:
            x_list.append(int(line[itr])-493)
        else:
            x_list.append(int(line[itr]))
        y_list.append(int(line[itr+1]))
    for itr in range(num_pairs - 1):
        image = draw(x_list[itr], y_list[itr], x_list[itr + 1], y_list[itr + 1], image)

# Determines where the sand grain ends up
def recursive_sand_drop(sand_down, sand_right, image):
    # print(sand_down, sand_right)
    if sand_down == image.shape[0] - 1:
        changing_grain_structure = False
        return image, changing_grain_structure
    if image[sand_down + 1, sand_right] == '.': #Nothing below
        return recursive_sand_drop(sand_down + 1, sand_right, image)
    if image[sand_down + 1, sand_right - 1] == '.': #Move sand to the left
        return recursive_sand_drop(sand_down + 1, sand_right - 1, image)
    if image[sand_down + 1, sand_right + 1] == '.': #Move sand to the right
        return recursive_sand_drop(sand_down + 1, sand_right + 1, image)
    if (sand_down == drop_point[0]) & (sand_right == drop_point[1]):
        changing_grain_structure = False
        return image, changing_grain_structure
    image[sand_down, sand_right] = 'o'
    changing_grain_structure = True
    return image, changing_grain_structure
    

changing_grain_structure = True
grain_count = 0
while changing_grain_structure:
    image, changing_grain_structure = recursive_sand_drop(drop_point[0], drop_point[1], image)
    grain_count += 1
    
print('Part 1: ', grain_count - 1)




##### Part 2 #####

if test:
    lines = ["498,4 -> 498,6 -> 496,6", "503,4 -> 502,4 -> 502,9 -> 494,9"] 
    image = np.full((13, 24), '.')
    drop_point = (0, 12)
else:
    with open('./input.txt') as file:
        lines = file.read().splitlines()
    image = np.full((600,6000), '.')
    drop_point = (0, 3500)


# Draws the walls of image
max_y = 0
for line in lines:
    line  = line.replace(" -> ", ",")
    line = line.split(",")
    x_list = []
    y_list = []
    num_pairs = int(len(line) / 2)
    for itr in range(0, num_pairs * 2, 2):
        if test:
            x_list.append(int(line[itr])-488)
        else:
            x_list.append(int(line[itr])+3000)
        y_list.append(int(line[itr+1]))
    if max(y_list) > max_y:
        max_y = max(y_list)
    for itr in range(num_pairs - 1):
        image = draw(x_list[itr], y_list[itr], x_list[itr + 1], y_list[itr + 1], image)
 
 
 
floor_height = max_y + 2 

image = draw(0, floor_height, image.shape[1], floor_height, image)

changing_grain_structure = True
grain_count = 0
while changing_grain_structure:
    image, changing_grain_structure = recursive_sand_drop(drop_point[0], drop_point[1], image)
    grain_count += 1
    print(grain_count)
    
print('Part 2: ', grain_count)
  

