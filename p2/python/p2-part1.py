def get_input(filename: str) -> list:
    with open (filename) as f:
        return f.readlines()


def process_game(game: str, constraints: dict) -> (bool, int):
    splits = game.split(":")
    game_id, game_pulls = int(''.join(filter(str.isdigit, splits[0]))), splits[1].split(";")

    # Each game can have multiple "pulls" that need to be checked for validity 
    for pull in game_pulls:
        pull = pull.strip()

        # Incase of trailing ; there may be an empty string we want to skip
        if not pull:
            continue
        
        color_groups = pull.split(",")

        for pair in color_groups:
            parts = pair.strip().split(" ")
            count, color = int(parts[0]), parts[1]
            
            if count > constraints[color]:
                return (False, 0)
    
    return (True, game_id)
        

if __name__ == "__main__":
    filename = "/mnt/workspace/adventofcode23/p2/input.txt"

    constraints = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    sum_game_ids = 0

    for game in get_input(filename):
        results = process_game(game, constraints)
        if results[0]:
            sum_game_ids += results[1]

    print(sum_game_ids)
