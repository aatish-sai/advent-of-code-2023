def solve(filename):
    input = []

    with open(filename, 'r') as file:
        while line := file.readline():
            row = [x for x in line.strip()]
            input.append(row)

    columns = len(input[0])
    rows = len(input)

    result = 0
    for c in range(columns):
        placement_points = rows
        for r in range(rows):
            if input[r][c] == 'O':
                result += placement_points
                placement_points -= 1
            if input[r][c] == '#':
                placement_points = rows - r - 1
    print(result)


solve("test.txt")
solve("input.txt")
