'''
Greedy approach
    - 1 loops
    - O(1) space (or O(n)?)
    - O(n) time
    - considers only +ve ints
'''

def pushDownValues(items, fromIndex):
    # loop in reverse starting from end of array till the 'fromIndex' where the 'push down' should start
    for i in range(len(items) - 1, fromIndex, -1):
        items[i] = items[i-1]
    print(f"After push: {items[0]}, {items[1]}, {items[2]}: {fromIndex}")

def sort_max(current_value):
    print(f"Begin iteration values (max): {max_list[0]}, {max_list[1]}, {max_list[2]}; {current_value}")

    # if we already have the number in the max list then skip
    if (current_value in max_list):
        continue

    # we cannot use >= because if the item is already in max_list (for eg the initial values)
    # then we'll still push down values
    # if we use > then make sure we check for 'current_value in max_list' above - otherwise
    # when current_value equals one of the values it is checked against next one and might 
    # be added again
    if (current_value > max_list[0]):
        pushDownValues(max_list, 0)
        max_list[0] = current_value
    elif (current_value > max_list[1]):
        pushDownValues(max_list, 1)
        max_list[1] = current_value
    elif (current_value > max_list[2]):
        max_list[2] = current_value

    print(f"End iteration values (max): {max_list[0]}, {max_list[1]}, {max_list[2]}; {current_value}")
    print("-------------------------------------")

def sort_min(current_value):
    print(f"Begin iteration values (min): {min_list[0]}, {min_list[1]}, {min_list[2]}; {current_value}")

    if (current_value <= min_list[0]):
        pushDownValues(min_list, 0)
        min_list[0] = current_value
    elif (current_value <= min_list[1]):
        pushDownValues(min_list, 1)
        min_list[1] = current_value
    elif (current_value <= min_list[2]):
        min_list[2] = current_value

    print(f"End iteration values (min): {min_list[0]}, {min_list[1]}, {min_list[2]}; {current_value}")
    print("-------------------------------------")

def find_max_prod(min_list, max_list):
    ''' 
    Logic - take products of:
        a) All items in max_list
        b) First 2 items in min_list & 1st item in max_list -> if we have two large -ve numbers
        c) return the max of a & b
    '''
    positive_max = max_list[0] * max_list[1] * max_list[2]
    negative_max = min_list[0] * min_list[1] * max_list[0]

    return max(positive_max, negative_max)


if __name__ == "__main__":
    int_list = [15, 10, 7, 8, 5, 11, 12, 9, 6, -12, -13]
    # int_list = [1, 2, 5, 6, 7, 8, 9, 10, 4, 77]

    max_list = int_list[:3]
    max_list.sort(reverse = True)

    min_list = int_list[:3]
    min_list.sort()

    print(f"Initial max values: {max_list[0]}, {max_list[1]}, {max_list[2]}")
    print(f"Initial min values: {min_list[0]}, {min_list[1]}, {min_list[2]}")
    print("-------------------------------------")

    for i in range(3, len(int_list)):
        current_value = int_list[i]
        
        sort_max(current_value)
        sort_min(current_value)

        max_product = find_max_prod(min_list, max_list)


    print(f"Final values: {max_list[0]}, {max_list[1]}, {max_list[2]}")
    print(f"Final values: {min_list[0]}, {min_list[1]}, {min_list[2]}")
    print(f"Max product: {max_product}")

