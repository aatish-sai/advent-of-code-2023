from typing import OrderedDict


def get_value(input):
    value = 0
    for i in input:
        value += ord(i)
        value *= 17
        value = value % 256
    return value


def solve(filename):
    with open(filename, "r") as file:
        input = [x.strip() for x in file.readlines()]

    result = 0
    for i in input[0].split(','):
        result += get_value(i)
    print(result)


def solve2(filename):
    with open(filename, "r") as file:
        input = [x.strip() for x in file.readlines()]

    light_box = {}
    for i in input[0].split(','):
        box_no = get_value(i.split('-')[0].split('=')[0])
        if box_no not in light_box:
            light_box[box_no] = OrderedDict()
        if '-' in i:
            len = i.split('-')[0]
            lens = light_box[box_no].keys()
            if len in lens:
                light_box[box_no].pop(len)
        if '=' in i:
            len, focal = i.split('=')
            lens = light_box[box_no].keys()
            light_box[box_no][len] = focal

    value = 0

    for box_no, box in light_box.items():
        for idx, len in enumerate(box.values()):
            value += int(box_no + 1) * int(idx + 1) * int(len)
    print(value)


solve("test.txt")
solve("input.txt")

solve2("test.txt")
solve2("input.txt")
