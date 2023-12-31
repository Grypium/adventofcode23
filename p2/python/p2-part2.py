def get_input(filename: str) -> list:
    with open (filename) as f:
        return f.readlines()


def process_game(game: str) -> (int):
    splits = game.split(":")
    game_id, game_pulls = int(''.join(filter(str.isdigit, splits[0]))), splits[1].split(";")
    
    minimum_cubes = {
        "red": 0,
        "blue":0,
        "green": 0
    }

    # Each game can have multiple "pulls" that need to be checked for minimum number of cubes 
    for pull in game_pulls:
        pull = pull.strip()

        # Incase of trailing ; there may be an empty string we want to skip
        if not pull:
            continue
        
        color_groups = pull.split(",")

        for pair in color_groups:
            parts = pair.strip().split(" ")
            count, color = int(parts[0]), parts[1]

            if minimum_cubes[color] < count:
                minimum_cubes[color] = count
    
    power_of_set_of_cubes = 1
    for color in minimum_cubes:
        power_of_set_of_cubes *= minimum_cubes[color]

    return power_of_set_of_cubes
        

if __name__ == "__main__":
    filename = "/mnt/workspace/adventofcode23/p2/input.txt"

    constraints = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    sum_powers = 0

    for game in get_input(filename):
        results = process_game(game)
        sum_powers += results

    print(sum_powers)
