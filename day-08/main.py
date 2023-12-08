def solve(filename):
    movement = None
    nodes = {}
    with open(filename, "r") as file:
        while line := file.readline():
            if not movement:
                movement = line.strip()
                continue
            if line.strip() == '':
                continue

            root, children = line.split(" = ")
            left, right = children[1:-2].split(", ")

            if root not in nodes:
                nodes[root.strip()] = [left.strip(), right.strip()]
    
    start = 'AAA'
    steps = 0
    final = False
    direction_code = {
    'L': 0,
    'R': 1
    }
    while not final:
        for direction in movement:
            steps += 1
            if nodes[start][direction_code[direction]] == 'ZZZ':
                final = True
            else:
                start = nodes[start][direction_code[direction]]
            
    print(steps)

def solve2(filename):
    movement = None
    nodes = {}
    with open(filename, "r") as file:
        while line := file.readline():
            if not movement:
                movement = line.strip()
                continue
            if line.strip() == '':
                continue

            root, children = line.split(" = ")
            left, right = children[1:-2].split(", ")

            if root not in nodes:
                nodes[root.strip()] = [left.strip(), right.strip()]

    starts = [x for x in nodes.keys() if x[-1] == 'A']
    steps = 0
    final = False
    direction_code = {
    'L': 0,
    'R': 1
    }
    

    processed_node = {}

    for key, value in nodes.items():
        has_z = False
        start = key
        dest = ''
        pos = 0
        zpos = []
        for direction in movement:
            pos += 1
            dest = nodes[start][direction_code[direction]]
            start = dest
            if dest[-1] == 'Z':
                has_z = True
                zpos.append(pos)

        processed_node[key] = {
            "destination": dest,
            "zpath": has_z,
            "zlocation": zpos
        }

    meta = []
    for idx, start in enumerate(starts):
        begins = start
        pos = 0
        while True:
            if processed_node[begins]["zpath"] == True:
                meta.append(pos + processed_node[begins]["zlocation"][0])
                break
            else:
                begins = processed_node[begins]["destination"]
            pos += len(movement)
    from math import lcm
    print(lcm(*meta))


    # BruteForcing does not work :(
    # while not final:
    #     print("crrent steps ", steps)
    #     zpos = []
    #     need_checking = True
    #     for idx, start in enumerate(starts):
    #         if processed_node[start]["zpath"] == False:
    #             need_checking = False
    #         else:
    #             zpos.append(processed_node[start]["zlocation"])
    #         starts[idx] = processed_node[start]["destination"]
    #
    #     if need_checking:
    #         intersetion_result = set(zpos[0]).intersection(*zpos[1:])
    #
    #         if len(intersetion_result) > 0:
    #             final = True
    #             print(steps + min(intersetion_result))
    #             break
    #     steps += len(movement)

if __name__ == "__main__":
    solve("test.txt")
    solve("test2.txt")
    solve("input.txt")

    solve2("test3.txt")
    solve2("input.txt")
