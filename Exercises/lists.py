def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    x = list((number,))
    x.extend([number+1, number+2])
    return x



def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    avg_odd = sum(hand[::2])/len(hand[::2])
    avg_even = sum(hand[1::2])/len(hand[1::2])

    return avg_odd == avg_even

print(average_even_is_average_odd([1, 2, 3]))