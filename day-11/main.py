def solve(filename):
    no_galaxy_row = []
    no_galaxy_col = []
    galaxy_no = 1
    galaxy = {}
    with open(filename, "r") as file:
        row = 0
        col_status = []
        while line := file.readline():
            if '#' not in line:
                no_galaxy_row.append(row)

            else:
                for idx, x in enumerate(line.strip()):
                    if row == 0:
                        col_status.append(True)
                    if x == '#':
                        col_status[idx] = col_status[idx] and False
                        galaxy[galaxy_no] = [row, idx]
                        galaxy_no += 1
                    else:
                        col_status[idx] = col_status[idx] and True
            row += 1

    for idx, x in enumerate(col_status):
        if x:
            no_galaxy_col.append(idx)

    # generate combination between the galaxy
    from itertools import combinations

    galaxy_combinations = combinations(galaxy.keys(), 2)
    result = 0
    result2 = 0
    for g_x, g_y in galaxy_combinations:
        a, b = galaxy[g_x]
        x, y = galaxy[g_y]

        no_expansion_distance = abs(y-b) + abs(x-a)

        expanded_row = [r for r in no_galaxy_row if r >
                        min(a, x) and r < max(a, x)]
        expanded_col = [c for c in no_galaxy_col if c >
                        min(b, y) and c < max(b, y)]
        distance = no_expansion_distance + \
            len(expanded_row) + len(expanded_col)
        result += distance

        distance2 = no_expansion_distance + 999_999 * \
            len(expanded_row) + 999_999*len(expanded_col)
        result2 += distance2

    print(result)
    print(result2)


solve("test.txt")
solve("input.txt")
