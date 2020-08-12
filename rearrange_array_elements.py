def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) <= 1:
        return [-1,-1]

    freq = [0 for _ in range(0,10)]
    for i in input_list:
        freq[i] += 1

    num1 = ''
    num2 = ''
    idx = 9

    while idx >= 0:
        if freq[idx] == 0:
            idx -= 1
            continue
        if len(num1) > len(num2):
            num2 += str(idx)
        else:
            num1 += str(idx)
        
        freq[idx] -= 1
    
    return [int(num1),int(num2)]
        

if __name__ == "__main__":

    def test_function(test_case):
        output = rearrange_digits(test_case[0])
        solution = test_case[1]
        if sum(output) == sum(solution):
            print("Pass")
        else:
            print("Fail")

    test_function([[1, 2, 3, 4, 5], [542, 31]])
    test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]

        #Array not inverted
    print('--Test 1--')
    print('Value: {}'.format(rearrange_digits([1,2,3,4,5,6,7])))
    print('Expected: {}'.format([7531,642]))

    print('--Test 2--')
    print('Value: {}'.format(rearrange_digits([0])))
    print('Expected: {}'.format([-1,-1]))

    print('--Test 3--')
    print('Value: {}'.format(rearrange_digits([])))
    print('Expected: {}'.format([-1,-1]))

    print('--Test 4--')
    print('Value: {}'.format(rearrange_digits([9, 9, 4, 9, 3, 8, 6, 2])))
    print('Expected: {}'.format([9963, 9842]))