def isBrelan(hand):
    ranks = [card[0] for card in hand]
    for rank in set(ranks):
        if ranks.count(rank) >= 3:
            return True
    return False