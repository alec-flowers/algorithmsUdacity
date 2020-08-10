

def sqrt(number):
    """
    Calculate the floored square root of a number. Sovling using Newtons iterative method. 

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number <= 0:
        return 0
    if number <= 1:
        return 1

    x = number
    while int(x) != int(.5 * (x + number/x)):
        print(x)
        x = .5 * (x + number/x)

    return int(x)

if __name__ == "__main__":
    print('Calculated: {}  Expected: {}'.format(sqrt(25),5))
    print('Calculated: {}  Expected: {}'.format(sqrt(100),10))
    print('Calculated: {}  Expected: {}'.format(sqrt(3599),59))
    print('Calculated: {}  Expected: {}'.format(sqrt(0),0))
    print('Calculated: {}  Expected: {}'.format(sqrt(1),1))
    print('Calculated: {}  Expected: {}'.format(sqrt(928342),963))

