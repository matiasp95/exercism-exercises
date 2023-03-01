EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate the time in minutes it will take to prepare the lasagna with new layers.

    :param number_of_layers: int - number of layers to add to the lasagna
    :return: int - Time it will take to prepare the new layers (Based on PREPARATION_TIME constant)

    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate the total number of minutes you've been cooking.

    :param number_of_layers: int - number of layers you have added to the lasagna.
    :param elapsed_bake_time: int - time that has passed since the lasagna has been cooking.
    :return: int - Total elapsed time.

    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time