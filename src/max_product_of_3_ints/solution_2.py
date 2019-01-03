'''
Greedy approach
    - 1 loops
    - O(1) space (or O(n)?)
    - O(n) time
'''

def pushDownValues(items, fromIndex):
    for i in range(len(items) - 1, fromIndex + 1, -1):
        items[i] = items[i-1]

int_list = [15, 10, 7, 8, 5, 11,  12, 9]

max_list = int_list[:3]
max_list.sort(reverse = True)

print(f"Initial values: {max_list[0]}, {max_list[1]}, {max_list[2]}")
print("-------------------------------------")

for i in range(len(int_list) - 1):
    current_value = int_list[i]
    
    print(f"Begin iteration values: {max_list[0]}, {max_list[1]}, {max_list[2]}; {current_value}")

    if (current_value >= max_list[0]):
        pushDownValues(max_list, 0)
        max_list[0] = current_value
    elif (current_value >= max_list[1]):
        pushDownValues(max_list, 1)
        max_list[1] = current_value
    elif (current_value >= max_list[2]):
        max_list[2] = current_value

    print(f"End iteration values: {max_list[0]}, {max_list[1]}, {max_list[2]}; {current_value}")
    print("-------------------------------------")

print(f"Final values: {max_list[0]}, {max_list[1]}, {max_list[2]}")

