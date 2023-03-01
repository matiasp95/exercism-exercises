def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if(number < 0):
        # if a number to be classified is less than 1.
        raise ValueError("Classification is only possible for positive integers.")
    divid = []
    limit = (number//2)+1
    for i in range(1,limit):
        if(number%i == 0):
            divid.append(i)
    if(sum(divid)==number):
        return "perfect"
    if(sum(divid)>number):
        return "abundant"
    return "deficient"

print(classify(6))
