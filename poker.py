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

def value_of_hand(hand):
    if isBrelan(hand):
        return 30