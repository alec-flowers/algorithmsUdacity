def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) <= 0:
        return (None,None)

    min_ = ints[0]
    max_ = ints[0]

    for i in ints:
        if i > max_:
            max_ = i
        if i < min_:
            min_ = i

    return (min_, max_)


if __name__ == "__main__":
    ## Example Test Case of Ten Integers
    import random
    print('Vanilla Test Cases')
    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)

    print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

    print('--Test 1--')
    print('Value: {}'.format(get_min_max([200, 5, 1,-100, 4, 2, 95, 9, 1, 44, 34])))
    print('Expected: ({}, {})'.format(-100,200))

    print('--Test 2--')
    print('Value: {}'.format(get_min_max([0])))
    print('Expected: ({}, {})'.format(0,0))

    print('--Test 3--')
    print('Value: {}'.format(get_min_max([])))
    print('Expected: (None, None)')