CARDS = "  23456789TJQKA"
def best_hands(hands: list[str]) -> list[str]:
    ranked = [hand_evalutor(h) for h in hands]
    best = max(ranked)
    return [h for h, r in zip(hands, ranked) if r == best]
def hand_evalutor(hand: str) -> tuple[int, ...]:
    kinds = [CARDS.index(r) for r, _ in hand.replace("10", "T").split()]
    counts, ranks = zip(*sorted(((kinds.count(k), k) for k in set(kinds)), reverse=True))
    ranks = (5, 4, 3, 2, 1) if ranks == (14, 5 , 4, 3, 2) else ranks
    straight = len(counts) == 5 and (max(ranks) - min(ranks) == 4)
    flush = len(set(c[-1] for c in hand.split())) == 1
    category = (9 if counts == (5,) else #Five of a kind
                8 if straight and flush else #Straight flush
                7 if counts == (4, 1) else #Four of a kind
                6 if counts == (3, 2) else #Full house
                5 if flush else
                4 if straight else
                3 if counts[0] == 3 else
                2 if counts[: 2] == (2, 2) else
                1 if counts[0] == 2 else 
                0)
    return category, *ranks