GAME_CONSTRAINTS = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def check_game_validity(game):
    current_count = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    turns = game.split(", ")
    for turn in turns:
        for k in GAME_CONSTRAINTS.keys():
            if k in turn:
                current_count[k] += int(turn.split(" ")[0])
                if (current_count[k] >GAME_CONSTRAINTS[k]):
                    print("game no valid for", k)
                    return False
    return True

def get_required_cubes(game):
    result = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    
    turns = game.split(", ")
    for turn in turns:
        for k in result.keys():
            if k in turn:
                result[k] += int(turn.split(" ")[0])

    return result

def process_game(game_line, version = 'v1'):

    game_details, games = game_line.split(": ")
    game_id = int(game_details.split(" ")[-1])

    game_list = games.split("; ")

    if version == 'v1':
        for game in game_list:
            if not check_game_validity(game):
               return 0

        return int(game_id)

    if version == 'v2':
        current_count = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        for game in game_list:
            required_count = get_required_cubes(game)
            for key in current_count.keys():
                if current_count[key] < required_count[key]:
                    current_count[key] = required_count[key]

        result = 1
        for key in current_count.keys():
            result *= current_count[key]

        return int(result)

def solve(filename):
    result = 0
    with open(filename, "r") as file:
        while line := file.readline():
            value = process_game(line.strip())
            result += value

    print(result)


def solve2(filename):
    result = 0
    with open(filename, "r") as file:
        while line := file.readline():
            value = process_game(line.strip(), "v2")
            result += value

    print(result)

if __name__ == "__main__":
    solve2("test.txt")
    solve2("input.txt")
