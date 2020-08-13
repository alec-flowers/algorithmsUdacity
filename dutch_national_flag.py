def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    count_0 = 0
    count_1 = 0
    count_2 = len(input_list)-1

    while count_1 <= count_2:
        if input_list[count_1] == 0:
            input_list[count_1], input_list[count_0] = input_list[count_0], input_list[count_1]
            count_0 += 1
            count_1 += 1
        elif input_list[count_1] == 2:
            input_list[count_1], input_list[count_2] = input_list[count_2], input_list[count_1]
            count_2 -= 1
        else:
            count_1 += 1

    return input_list

if __name__ == "__main__":
    def test_function(test_case):
        sorted_array = sort_012(test_case)
        print(sorted_array)
        if sorted_array == sorted(test_case):
            print("Pass")
        else:
            print("Fail")

    print('Vanilla Test Cases')
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

    print('--Test 1--')
    print('Value: {}'.format(sort_012([2, 0, 0, 0])))
    print('Expected: {}'.format([0, 0, 0, 2]))

    print('--Test 2--')
    print('Value: {}'.format(sort_012([0])))
    print('Expected: {}'.format([0]))

    print('--Test 3--')
    print('Value: {}'.format(sort_012([])))
    print('Expected: {}'.format([]))