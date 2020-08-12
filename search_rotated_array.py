def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    start = 0
    end = len(input_list) - 1
    
    while start <= end:
        ##need to recalculate mid
        mid = start + (end-start) // 2

        if input_list[mid] == number:
            return mid
        if input_list[start] > input_list[mid]:
            #left size contains pivot & unordered list
            if (number > input_list[mid]) and (number <= input_list[end]):
                #check if number is between right side numbers (which we know is in order)
                start = mid + 1
            else:
                end = mid - 1
        else:
            if (number < input_list[mid]) and (number >= input_list[start]):
                #check if number is between left side numbers (which we know is in order)
                end = mid - 1
            else:
                start = mid + 1
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

if __name__ == "__main__":

    print('Vanilla Test Cases')
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])


    #Array not inverted
    print('--Test 1--')
    print('Value: {}'.format(rotated_array_search([1,2,3,4,5,6,7],7)))
    print('Expected: {}'.format(6))

    print('--Test 2--')
    print('Value: {}'.format(rotated_array_search([0],0)))
    print('Expected: {}'.format(0))

    print('--Test 3--')
    print('Value: {}'.format(rotated_array_search([],5)))
    print('Expected: {}'.format(-1))