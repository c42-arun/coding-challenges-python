'''
Brute force approach:
    - 3 loops
    - O(1) space (or O(n)?)
    - O(n*3) time
'''
int_list = [15, 10, 7, 8, 5, 11,  12, 9]

max_prod = int_list[0] * int_list[1] * int_list[2]

print('Initial max prod: ' + str(max_prod))

for i in range(len(int_list) - 2): # iterate till second to last
    for j in range(i+1, len(int_list) - 1):
        for k in range(j+1, len(int_list) ):
            current_prod = int_list[i] * int_list[j] * int_list[k]
            if (current_prod > max_prod):
                max_prod = current_prod
                print(max_prod)

print('Max prod: ' + str(max_prod))