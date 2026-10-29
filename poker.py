def isBrelan(hand):
    ranks = [card[0] for card in hand]
    for rank in set(ranks):
        if ranks.count(rank) >= 3:
            return True
    return False

def isFourOfAKind(hand):
    ranks = [card[0] for card in hand]
    for rank in set(ranks):
        if ranks.count(rank) >= 4:
            return True
    return False

def isFullHouse(hand):
    ranks = [card[0] for card in hand]
    has_three_of_a_kind = False
    has_pair = False

    for rank in set(ranks):
        count = ranks.count(rank)
        if count == 3:
            has_three_of_a_kind = True
        elif count == 2:
            has_pair = True

    return has_three_of_a_kind and has_pair

def isHighCard(hand):
    return True

def isStraight(hand):
    ranks = sorted([int(card[0]) for card in hand])
    for i in range(len(ranks) - 1):
        if ranks[i] + 1 != ranks[i + 1]:
            return False
    return True

def value_of_hand(hand):
    if isFourOfAKind(hand):
        return 60
    elif isFullHouse(hand):
        return 50
    elif isBrelan(hand):
        return 30
    elif isStraight(hand):
        return 40
    elif isHighCard(hand):
        ranks = [int(card[0]) for card in hand]
        return max(ranks)
