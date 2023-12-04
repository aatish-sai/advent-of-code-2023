def get_point(card):
    card_id, card_game = card.split(":")
    card_number = int(card_id.strip().split()[1])

    try:
        cards[card_number] += 1
    except:
        cards[card_number] = 1

    lottery, winning_lottery = card_game.strip().split("|")

    lottery_numbers = set(lottery.strip().split())
    winning_numbers = set(winning_lottery.strip().split())

    count = 0
    for number in lottery_numbers:
        if number in winning_numbers:
            count += 1
    for i in range(1, count + 1):
        try:
            cards[card_number + i] += cards[card_number]
        except:
            cards[card_number + i] = cards[card_number]
    if count == 0:
        return 0
    else:
        return 2**(count - 1)

def solve(filename):
    result = 0
    with open(filename, "r") as file:
        while line := file.readline():
            point = get_point(line)
            result += point

    print(result)
    count = 0
    for v in cards.values():
        count += v
    print(count)

if __name__ == "__main__":
    global cards
    cards = {}
    solve("test.txt")
    cards = {}
    solve("input.txt")
