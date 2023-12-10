def solve(filename):
    input = []
    perimeter = []
    with open(filename, "r") as file:
        row = 0
        start_pos = []
        while line := file.readline():
            input.append([*line.strip()])
            if 'S' in line:
                start_pos = [row, line.index('S')]
            row += 1

    max_row = len(input)
    max_col = len(input[0])

    perimeter.append(start_pos)

    def get_surrounding(x, y):
        surroundings = []

        possible = []
        available = [[x-1, y], [x, y-1], [x+1, y], [x, y+1]]

        for new_x, new_y in available:
            if new_x >= max_row or new_y >= max_col or new_x < 0 or new_y < 0:
                continue
            else:
                possible.append([new_x, new_y])

        for new_x, new_y in possible:
            if new_x == x and new_y > y:
                if input[new_x][new_y] in ['-', '7', 'J']:
                    surroundings.append([new_x, new_y])
                    continue
            if new_x == x and new_y < y:
                if input[new_x][new_y] in ['-', 'L', 'F']:
                    surroundings.append([new_x, new_y])
                    continue
            if new_x < x and new_y == y:
                if input[new_x][new_y] in ['|', '7', 'F']:
                    surroundings.append([new_x, new_y])
                    continue
            if new_x > x and new_y == y:
                if input[new_x][new_y] in ['|', 'L', 'J']:
                    surroundings.append([new_x, new_y])
                    continue
        return surroundings

    def next_pos(start, pipe):
        x, y = start
        pipe_x, pipe_y = pipe
        # pipe in vertical orinetation
        if y == pipe_y:
            if pipe_x > x:  # pipe is below
                if input[pipe_x][pipe_y] == '|':
                    return pipe_x + 1, pipe_y
                if input[pipe_x][pipe_y] == 'J':
                    return pipe_x, pipe_y - 1
                if input[pipe_x][pipe_y] == 'L':
                    return pipe_x, pipe_y + 1
            else:  # pipe is above
                if input[pipe_x][pipe_y] == '|':
                    return pipe_x - 1, pipe_y
                if input[pipe_x][pipe_y] == '7':
                    return pipe_x, pipe_y - 1
                if input[pipe_x][pipe_y] == 'F':
                    return pipe_x, pipe_y + 1
        # pipe in horizionla orientation
        else:
            if pipe_y > y:  # pipe is to the right
                if input[pipe_x][pipe_y] == '-':
                    return pipe_x, pipe_y + 1
                if input[pipe_x][pipe_y] == 'J':
                    return pipe_x - 1, pipe_y
                if input[pipe_x][pipe_y] == '7':
                    return pipe_x + 1, pipe_y
            else:  # pipe is to the left
                if input[pipe_x][pipe_y] == '-':
                    return pipe_x, pipe_y - 1
                if input[pipe_x][pipe_y] == 'L':
                    return pipe_x - 1, pipe_y
                if input[pipe_x][pipe_y] == 'F':
                    return pipe_x + 1, pipe_y

    valid_starts = get_surrounding(*start_pos)

    steps = 1
    current = start_pos
    pipe = valid_starts[0]
    perimeter.append(valid_starts[0])

    while True:
        next_p = next_pos(current, pipe)
        steps += 1
        current, pipe = pipe, next_p

        if input[next_p[0]][next_p[1]] == 'S':
            break

        perimeter.append([next_p[0], next_p[1]])
    print(steps/2)


if __name__ == "__main__":
    solve("test.txt")
    solve("test2.txt")
    solve("input.txt")
