game_input = []

def get_number_loc_from_line(line):
    response = []
    current = []
    for idx, char in enumerate(line):
        if char.isnumeric():
            current.append(idx)
        else:
            if len(current) > 0:
                response.append(current)
            current = []
        if idx == len(line) - 1:
            response.append(current)
    return response

def get_surrounding(row, cols):
    surrounding = []
    for idx, col in enumerate(cols):
        if idx == 0:
            surrounding.append([row-1, col-1])
            surrounding.append([row, col-1])
            surrounding.append([row+1, col-1])
        surrounding.append([row-1, col])
        surrounding.append([row+1, col])
        if idx == len(cols) - 1:
            surrounding.append([row-1, col+1])
            surrounding.append([row, col+1])
            surrounding.append([row+1, col+1])
    return surrounding

def get_value(row, number):
    global game_input
    value = 0
    for idx, col in enumerate(number):
        value += int(game_input[row][col]) * 10**(len(number) - 1 - idx)

    return value

def check_validity(idx, number):
    value = get_value(idx, number)
    surroundings = get_surrounding(idx, number)
    for row, column in surroundings:
        if row < 0 or column < 0 or row >= len(game_input) or column >= len(game_input[0]):
            continue
        if game_input[row][column] != '.' and not game_input[row][column].isalnum():
            return True, value
    return False, value

possible_gears = {}

def check_for_possible_gears(idx, number):
    global possible_gears
    value = get_value(idx, number)
    surroundings = get_surrounding(idx, number)
    for row, column in surroundings:
        if row < 0 or column < 0 or row >= len(game_input) or column >= len(game_input[0]):
            continue
        if game_input[row][column] == '*':
            try:
                possible_gears[f"{row}-{column}"].append(value)
            except KeyError:
                possible_gears[f"{row}-{column}"] = [value]

def compute_with_gear_value():
    global possible_gears
    gears = [v for v in possible_gears.values() if len(v) == 2 ]

    gear_ratio_value = 0

    for real_gears in gears:
        gear_ratio_value += (real_gears[0] * real_gears[1])
    return gear_ratio_value

def process_game(input):
    global game_input
    game_input = [line.strip() for line in input]

    result = 0
    invalid = 0
    for idx, line in enumerate(input):
        numbers = get_number_loc_from_line(line.strip())
        for number in numbers:
            valid, val = check_validity(idx, number)
            if valid:
                result += val
            else:
                invalid += val
            check_for_possible_gears(idx, number)

    return result

def solve(filename):
    with open(filename, "r") as file:
        input = file.readlines()
        result = process_game(input)
    print(result)

    result_v2 = compute_with_gear_value()
    print(result_v2)

if __name__ == "__main__":
    solve("input.txt")
