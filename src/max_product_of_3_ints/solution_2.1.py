'''
Greedy approach
    - 1 loops
    - O(1) space (or O(n)?)
    - O(n) time
    - considers only +ve ints
'''

def pushDownValues(items, fromIndex):
    print(f"Before push: {items[0]}, {items[1]}, {items[2]}: {fromIndex}")
    for i in range(len(items) - 1, fromIndex, -1):
        print(f"{i - 1} -> {i}")
        items[i] = items[i-1]
    print(f"After push: {items[0]}, {items[1]}, {items[2]}: {fromIndex}")

int_list = [-15, -10, 7, 8, 5, 11,  12, 9]

max_list = int_list[:3]
max_list.sort(reverse = True)

print(f"Initial values: {max_list[0]}, {max_list[1]}, {max_list[2]}")
print("-------------------------------------")

for i in range(len(int_list)):
    current_value = int_list[i]
    
    print(f"Begin iteration values: {max_list[0]}, {max_list[1]}, {max_list[2]}; {current_value}")

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

    print(f"End iteration values: {max_list[0]}, {max_list[1]}, {max_list[2]}; {current_value}")
    print("-------------------------------------")

print(f"Final values: {max_list[0]}, {max_list[1]}, {max_list[2]}")

