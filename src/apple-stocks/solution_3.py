prices = [15, 10, 7, 8, 5, 11,  12, 9]

# prices.sort(reverse = True)
# print(prices)

min_price = prices[0]               # initialize to first item
max_profit = prices[1] - prices[0]  # initialize to first sell/buy
print('Initial max profit '+ str(max_profit))

'''
Here we are seeing for iteration:
    - if iteration profit is more than current max profit so far
    - reset min_price to iteration price if lower (ready for next iteration)
Space complexity: O(1)
Time complexity: O(n) - only one loop
'''
for i in range(1, len(prices)):
    current_price = prices[i]
    potential_profit = current_price - min_price
    
    if (potential_profit > max_profit):
        max_profit = potential_profit
        print('Max profit: ' + str(max_profit))

    if (current_price < min_price):
        min_price = current_price
        print('Min price:' + str(min_price))

print('Max profit is ' + str(max_profit))


''' 
Follow up:

1.      You can't just take the difference between the highest price and the lowest price, 
        because the highest price might come before the lowest price. And you have to buy before you can sell.
        Satisfied

2.      What if the price goes down all day? In that case, the best profit will be negative.
        SATISFIED - there's no need to check for +ve profit in line 11

3.      Done in O(1) space and O(n) time
        O(1) space - yes (assuming its the additional space taken by algorithm which is always those temp vars max_profit, buy_price etc)
        O(n) time - yes, yes & yes

'''
