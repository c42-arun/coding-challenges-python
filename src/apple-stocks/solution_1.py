prices = [15,10, 7, 8, 5, 11,  12, 9, 7]
profits = [] # copy of original array so O(2n) space

# here we are seeing for each price (buy price) the maximum price 
# that occurs after (sell price)
# Space complexity: O(2n) ~ O(n) - as we make a copy of the list as profits list with n-1 items
# Time complexity: O(n) - only one loop (not sure about taking max() at each iteration?)
for i in range(len(prices) - 1):
    buy_price = prices[i]
    max_sell_price = max(prices[i+1:])
    if (max_sell_price > buy_price):
        profits.append(max_sell_price - buy_price)

max_profit = max(profits)

print('Max profit is ' + str(max_profit))


''' 
Follow up:

1.      You can't just take the difference between the highest price and the lowest price, 
        because the highest price might come before the lowest price. And you have to buy before you can sell.
        Satisfied

2.      What if the price goes down all day? In that case, the best profit will be negative.
        NOT SATISFIED - there's no need to check for +ve profit in line 11
        
'''