import itertools


def get_arrangement(input):
    result = []
    count = 0
    for c in input:
        if c == '.' and count > 0:
            result.append(count)
            count = 0
        if c == '#':
            count += 1
    if count > 0:
        result.append(count)

    return result


def replace_unknown(input, replacement):
    result = input
    for c in replacement:
        result = result.replace('?', c, 1)

    return result


def get_unknown_number(input):
    return input.count('?')


def get_solution(input):
    choice = '.#'
    puzzle, expected = input.split()
    expected_result = [int(i) for i in expected.split(',')]

    unknown = get_unknown_number(puzzle)

    ways = 0
    for i in itertools.product(choice, repeat=unknown):
        generated = replace_unknown(puzzle, list(i))
        output = get_arrangement(generated)

        if output == expected_result:
            ways += 1
    return ways


def solve(filename):
    result = 0
    with open(filename, 'r') as file:
        while line := file.readline():
            result += get_solution(line.strip())

    print(result)


solve("input.txt")
