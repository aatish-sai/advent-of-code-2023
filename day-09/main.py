def get_num(line):
    next_num = 0
    prev_num = 0
    line = list(map(int, line.split()))
    plus =True
    while True:
        new_line = [a-b for a, b in zip(line[1:], line[:-1])]
        next_num += line[-1]
        if plus:
            prev_num += line[0]
        else:
            prev_num -= line[0]
        plus = not plus
        if not any(new_line):
            break
        else: 
            line = new_line
    return prev_num , next_num


def solve(filename):
    result = 0
    result2 = 0
    with open(filename, "r") as file:
        while line := file.readline():
            prev_num, next_num = get_num(line.strip())
            result += next_num
            result2 += prev_num
    print(result, result2)

if __name__ == "__main__":
    solve("test.txt")
    solve("input.txt")
