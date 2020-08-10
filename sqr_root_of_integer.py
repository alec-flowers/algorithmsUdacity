

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

    x = number
    while int(x) != int(.5 * (x + number/x)):
        x = .5 * (x + number/x)

    return int(x)


print(sqrt(100))


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")