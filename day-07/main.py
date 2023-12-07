CARD_STRENTGH = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
CARD_STRENTGH_V2 = ['A','K','Q','T','9','8','7','6','5','4','3','2', 'J']

def compare_hands(hand1, hand2):
    a = hand1[0]
    b = hand2[0]
    for i in range(5):
        if CARD_STRENTGH.index(a[i]) > CARD_STRENTGH.index(b[i]):
            return 1
        elif CARD_STRENTGH.index(a[i]) < CARD_STRENTGH.index(b[i]):
            return -1
    return 0

def compare_hands_v2(hand1, hand2):
    a = hand1[0]
    b = hand2[0]
    for i in range(5):
        if CARD_STRENTGH_V2.index(a[i]) > CARD_STRENTGH_V2.index(b[i]):
            return 1
        elif CARD_STRENTGH_V2.index(a[i]) < CARD_STRENTGH_V2.index(b[i]):
            return -1
    return 0

from functools import cmp_to_key
card_cmp_key = cmp_to_key(compare_hands)
card_cmp_key_v2 = cmp_to_key(compare_hands_v2)
       

def check_hand_type_v2(hand):
    two_pairs = 0
    three_pairs = 0
    four_pairs = 0

    no_of_jokers = hand.count('J')

    for card in set(hand):
        if card == 'J':
            continue
        if list(hand).count(card) == 5:
            return "5_OF_A_KIND"
        elif list(hand).count(card) == 4:
            four_pairs += 1
        if list(hand).count(card) == 2:
            two_pairs += 1
        elif list(hand).count(card) == 3:
            three_pairs += 1

    if no_of_jokers > 3:
        return "5_OF_A_KIND"
    if no_of_jokers == 3 and two_pairs == 1:
        return "5_OF_A_KIND"
    if no_of_jokers == 3 and two_pairs == 0:
        return "4_OF_A_KIND"
    if no_of_jokers == 2 and three_pairs == 1:
        return "5_OF_A_KIND"
    if no_of_jokers == 2 and two_pairs == 1:
        return "4_OF_A_KIND"
    if no_of_jokers == 2 and three_pairs == 0 and two_pairs == 0:
        return "THREE_OF_A_KIND"
    if no_of_jokers == 1 and four_pairs == 1:
        return "5_OF_A_KIND"
    if no_of_jokers == 1 and three_pairs == 1:
        return "4_OF_A_KIND"
    if no_of_jokers == 1 and two_pairs == 2:
        return "FULL_HOUSE"
    if no_of_jokers == 1 and two_pairs == 1:
        return "THREE_OF_A_KIND"
    if no_of_jokers == 1 and two_pairs == 0 and three_pairs ==0 and four_pairs == 0:
        return "ONE_PAIR"
    if no_of_jokers == 0:
        if four_pairs == 1:
            return "4_OF_A_KIND"
        if (three_pairs == 1 and two_pairs == 1):
            return "FULL_HOUSE"
        if (three_pairs > 0 and two_pairs == 0):
            return 'THREE_OF_A_KIND'
        if (two_pairs == 2):
            return "TWO_PAIR"
        if (two_pairs == 1):
            return "ONE_PAIR"
    return "HIGH_CARD"

def check_hand_type(hand):
    two_pairs = 0
    three_pairs = 0


    for card in set(hand):
        if list(hand).count(card) == 5:
            return "5_OF_A_KIND"
        elif list(hand).count(card) == 4:
            return "4_OF_A_KIND"
        if list(hand).count(card) == 2:
            two_pairs += 1
        elif list(hand).count(card) == 3:
            three_pairs += 1

    if (three_pairs == 1 and two_pairs == 1):
        return "FULL_HOUSE"

    if (three_pairs > 0 and two_pairs == 0):
        return 'THREE_OF_A_KIND'

    if (two_pairs == 2):
        return "TWO_PAIR"
    if (two_pairs == 1):
        return "ONE_PAIR"

    return "HIGH_CARD"

def solve(filename):
    card_groups = {
        '5_OF_A_KIND': [],
        '4_OF_A_KIND': [],
        'FULL_HOUSE': [],
        'THREE_OF_A_KIND': [],
        'TWO_PAIR': [],
        'ONE_PAIR': [],
        'HIGH_CARD': []
    }
    with open(filename, 'r') as file:
        while line := file.readline():
            hand, bet = line.strip().split()
            hand_type = check_hand_type(hand)
            card_groups[hand_type].append((hand, bet))
   
    required_order = []
    for key, value in card_groups.items():
        if len(value) == 0:
            continue
        if len(value) > 1:
            value.sort(key=card_cmp_key)
            required_order += value
        else:
            required_order += value
    result = 0
    for i, value in enumerate(required_order):
        result += (len(required_order) - i) * int(value[1])

    print(result)

def solve_v2(filename):
    card_groups = {
        '5_OF_A_KIND': [],
        '4_OF_A_KIND': [],
        'FULL_HOUSE': [],
        'THREE_OF_A_KIND': [],
        'TWO_PAIR': [],
        'ONE_PAIR': [],
        'HIGH_CARD': []
    }
    with open(filename, 'r') as file:
        while line := file.readline():
            hand, bet = line.strip().split()
            hand_type = check_hand_type_v2(hand)
            card_groups[hand_type].append((hand, bet))
   
    required_order = []
    for key, value in card_groups.items():
        if len(value) == 0:
            continue
        if len(value) > 1:
            value.sort(key=card_cmp_key_v2)
            required_order += value
        else:
            required_order += value
    result = 0
    for i, value in enumerate(required_order):
        result += (len(required_order) - i) * int(value[1])

    print(result)

if __name__ == "__main__":
    solve("test.txt")
    solve("input.txt")
    solve_v2("test.txt")
    solve_v2("input.txt")
