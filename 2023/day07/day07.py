from collections import defaultdict


def main(data):
    hands = []
    for line in data:
        cards_count = defaultdict(int)
        cards, bid = line.split()
        for card in cards:
            cards_count[card] += 1
        if 5 in cards_count.values():
            hands.append((cards, bid, 6))
        elif 4 in cards_count.values():
            hands.append((cards, bid, 5))
        elif 3 in cards_count.values() and 2 in cards_count.values():
            hands.append((cards, bid, 4))
        elif 3 in cards_count.values():
            hands.append((cards, bid, 3))
        elif 2 in cards_count.values():
            number_of_2 = 0
            for count in cards_count.values():
                if count == 2:
                    number_of_2 += 1
            hands.append((cards, bid, number_of_2))
        else:
            hands.append((cards, bid, 0))

    sorted_hands = list()
    CARDS = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
    }
    print(len(hands))
    for hand in hands:
        found = False
        for index in range(len(sorted_hands)):
            if hand[2] < sorted_hands[index][2]:
                sorted_hands.insert(index, hand)
                found = True
                break
            if (
                hand[2] == sorted_hands[index][2]
            ):
                for card_a, card_b in zip(hand[0], sorted_hands[index][0]):
                    if card_a == card_b:
                        continue
                    else:
                        if CARDS[card_a] < CARDS[card_b]:
                            sorted_hands.insert(index, hand)
                            found = True
                            break
                        else:
                            break
                if found:
                    break
        if not found:
            sorted_hands.append(hand)

    total_winnings = 0
    for index in range(len(sorted_hands)):
        print(f"{index + 1}: {sorted_hands[index]}")
        total_winnings += (index + 1) * int(sorted_hands[index][1])
    
    print(f"Part 1: {total_winnings}")
    pass


def main2(data):
    hands = []
    for line in data:
        cards_count = defaultdict(int)
        cards, bid = line.split()
        jokers = 0
        for card in cards:
            if card != "J":
                cards_count[card] += 1
            else:
                jokers += 1
        # print(cards, jokers)
        # print(cards_count, end = ' ')
        # print(list(cards_count.values()), end = ' ')
        if len(cards_count) == 0:
            second_max = 0
            first_max = 0
        elif len(cards_count) == 1:
            second_max = 0
            first_max = list(cards_count.values())[0]
            # print(first_max)
        else:
            second_max, first_max = sorted(cards_count.values())[-2:]
        
        if first_max + jokers == 5:
            hands.append((cards, bid, 6))
        elif first_max + jokers == 4:
            hands.append((cards, bid, 5))
        elif first_max + jokers == 3 and second_max == 2:
            hands.append((cards, bid, 4))
        elif first_max + jokers == 3:
            hands.append((cards, bid, 3))
        elif first_max + jokers == 2 and second_max == 2:
            hands.append((cards, bid, 2))
        elif first_max + jokers == 2:
            hands.append((cards, bid, 1))
        else:
            hands.append((cards, bid, 0))
        print(hands[-1])
        
        
        
        # print(first_max, second_max)
        
        
    sorted_hands = list()
    CARDS = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 1,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
    }
    # print(len(hands))
    for hand in hands:
        found = False
        for index in range(len(sorted_hands)):
            if hand[2] < sorted_hands[index][2]:
                sorted_hands.insert(index, hand)
                found = True
                break
            if (
                hand[2] == sorted_hands[index][2]
            ):
                for card_a, card_b in zip(hand[0], sorted_hands[index][0]):
                    if card_a == card_b:
                        continue
                    else:
                        if CARDS[card_a] < CARDS[card_b]:
                            sorted_hands.insert(index, hand)
                            found = True
                            break
                        else:
                            break
                if found:
                    break
        if not found:
            sorted_hands.append(hand)

    total_winnings = 0
    for index in range(len(sorted_hands)):
        # print(f"{index + 1}: {sorted_hands[index]}")
        total_winnings += (index + 1) * int(sorted_hands[index][1])
    
    print(f"Part 2: {total_winnings}")
    pass


if __name__ == "__main__":
    lines = ""
    with open("input.txt", "r") as file:
        lines = file.readlines()
    # main(lines)
    main2(lines)
