def solve(filename):
    maps = {}
    inputs = []
    with open(filename, "r") as file:
        map_name = ''
        map_value = []
        while line := file.readline():
            if "seeds:" in line:
                inputs = [int(x) for x in line.strip().split(": ")[1].strip().split()]
            elif "map:" in line:
                map_name = line.strip().split()[0]
            elif len(line.strip()) == 0:
                if map_name != '':
                    maps[map_name] = map_value
                    map_name =  ''
                    map_value = []
            else:
                destination,source, lenght = [int(x) for x in line.strip().split()]
                map_value.append({
                           'source': source,
                           'destination': destination,
                           'range': lenght
                })
    def get_next_value(key, start):
        for x in maps[key]:
            if start >= x['source'] and start < x['source'] + x['range']:
                return x['destination'] + start - x['source']
        return start
    flows = ['seed-to-soil','soil-to-fertilizer','fertilizer-to-water','water-to-light','light-to-temperature','temperature-to-humidity','humidity-to-location']
    results = []
    for input in inputs:
        result = input
        for flow in flows:
            result = get_next_value(flow,result)

        results.append(result)
    print(min(results))
    
    results = []
    it = iter(inputs)
    for input in it:
        for x in range(input, input + next(it)):
            result = x
            for flow in flows:
                result = get_next_value(flow, result)
            results.append(result)

if __name__ == "__main__":
    solve("test.txt")
    solve("input.txt")
