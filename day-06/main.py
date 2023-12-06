def solve(input):
    result = 1
    for t, d in input:
        winning_ways = 0
        for i in range(t+1):
            if d < i * (t-i):
                winning_ways += 1
        result *= winning_ways

    return result

if __name__ == "__main__":
    print("TESTING")
    time = [7, 15, 30]
    distance = [9, 40, 200]

    input = zip(time, distance)
    
    answer = solve(input)

    print(answer)

    print("REAL INPUT")
    time = [52, 94, 75, 94]
    distance = [426, 1374, 1279, 1216]

    input = zip(time, distance)
    
    answer = solve(input)

    print(answer)


    print("TEST 2")
    time = [71530]
    distance = [940200]
    input = zip(time, distance)
    answer = solve(input)
    print(answer)

    
    print("REAL INPUT 2")
    time = [52947594]
    distance = [426137412791216]
    input = zip(time, distance)
    answer = solve(input)
    print(answer)
