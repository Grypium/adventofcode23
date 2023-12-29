

def get_first_num(s: str) -> str:
    for character in s:
        if character.isdigit():
            return character

def get_last_num(s: str) -> str:
    s = s[::-1]
    for character in s:
        if character.isdigit():
            return character

def get_input(filename: str) -> list:
    with open(filename) as f:
        return f.readlines()


if __name__ == "__main__":
    total = 0
    filename = "/mnt/workspace/adventofcode23/p1/input.txt"
    # ONLY FIRST NUMBER AND LAST NUMBER
    for line in get_input(filename):
        sum = int(get_first_num(line) + get_last_num(line))
        total += sum

    # OUR OUTPUT IS THE SUM OF ALL
    print("Total = " + str(total))

