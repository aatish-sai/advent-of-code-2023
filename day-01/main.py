def get_calibration_values(text):
    length = len(text)
    first = False
    first_value = 0
    first_pos = 0
    last = False
    last_value = 0
    last_pos = length - 1

    for i in range(length):
        if not first:
            if text[i].isnumeric():
                first = True
                first_value = int(text[i])

        if not last:
            if text[length-1-i].isnumeric():
                last = True
                last_value = int(text[length-1-i])

        if first and last:
            break

        if first and first_pos == length-1-i:
            break
        if last and last_pos == i:
            break
    value = 0
    if first:
        value = first_value * 10
    else:
        value = last_value *10

    if last:
        value = value + last_value
    else: 
        value = value + first_value

    return value

def solve(file):
    result = 0
    with open(file) as fp:
        while line := fp.readline():
            value = get_calibration_values(line.strip())
            result = result + value
    print(result)

if __name__ == "__main__":
    solve("input.txt")

