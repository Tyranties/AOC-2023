from typing import List

CARD_MAPPING = {'T': 'A', 'J': '.', 'Q': 'C', 'K': 'D', 'A': 'E'}


def classify_number(hand: str) -> int:
    counts = [hand.count(card) for card in hand]
    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts:
            return 4
        return 3
    if counts.count(2) == 4:
        return 2
    if 2 in counts:
        return 1
    return 0


def handle_j(hand: str) -> List[str]:
    if hand == "":
        return [""]

    return [x + y for x in ("23456789TQKA" if hand[0] == 'J' else hand[0]) for y in handle_j(hand[1:])]


def classify(hand: str) -> int:
    return max(map(classify_number, handle_j(hand)))


def sorting(hand: str) -> (int, List[str]):
    return classify(hand), [CARD_MAPPING.get(card, card) for card in hand]


plays = []

with open("day_07.txt", "r") as file:
    data = file.read().split("\n")
    for line in data:
        hand, bid = line.split()
        plays.append((hand, int(bid)))

plays.sort(key=lambda play: sorting(play[0]))

ans = 0

for rank, (hand, bid) in enumerate(plays, 1):
    ans += rank * bid

print(ans)