def get_input(filename: str) -> list:
    with open (filename) as f:
        return f.readlines()

def get_neighbors(cordinate: list, max_depth: int, max_width: int):
    neighbors = []
    y = cordinate[0]
    x = cordinate[1]

    # Check x boundaries
    # check x > 0 
    # check x < max_width
        
    # Check y boundaries
    # check y > 0 
    # check y < max_depth
    
    neighbors = []

    mods = [-1, 0, 1]
    
    for mod_x in mods:
        if mod_x + x < 0 or mod_x + x > max_width:
            continue
        for mod_y in mods:
            if mod_y == 0 and mod_x == 0:
                continue
            if mod_y + y < 0 or mod_y + y > max_depth:
                continue

            neighbors.append([mod_y + y, mod_x + x])
    
    return neighbors


def get_full_number(cordinate: list, grid: list):

    row = cordinate[0]
    index = cordinate[1]
    max_width = len(grid[0]) - 1

    forward_string = ""
    backward_string = ""

    # Forward
    forward_count = 1
    while True:
        f_index = index + forward_count
        if f_index > max_width:
            break

        char = grid[row][f_index]
        if char.isdigit():
            forward_string += char
            forward_count += 1
            continue
        break
    
    # Backwards
    backward_count = 1
    while True:
        b_index = index - backward_count
        if b_index < 0:
            break

        char = grid[row][b_index]
        if char.isdigit():
            backward_count += 1
            backward_string = char + backward_string
            continue
        break
    return int(backward_string + grid[row][index] + forward_string)

def get_symbols(grid: list):
    symbols = []
    
    for index_row, row in enumerate(grid):
        for index_column, column in enumerate(row):
            if not column.isalnum() and column != '.':
                cordinate = [index_row, index_column]
                symbols.append(cordinate)
    
    return symbols
                

if __name__ == "__main__": 
    input = get_input("/mnt/workspace/adventofcode23/p3/input.txt")
    input = [x.strip() for x in input]

    max_depth = len(input) - 1
    max_width = len(input[0]) - 1

    total = 0
    
    # symbols [[0,1], [9,3]]
    symbols = get_symbols(input)
    for symbol in symbols:
       neighbors = get_neighbors(symbol, max_depth, max_width)
       last_nums = []
       for neighbor in neighbors: 
           if input[neighbor[0]][neighbor[1]].isdigit():
               number = get_full_number(neighbor, input)
               if number in last_nums:
                   continue
                
               total += number
               last_nums.append(number)
               
    
    print(total)

