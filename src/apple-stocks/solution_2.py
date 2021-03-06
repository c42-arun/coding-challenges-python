prices = [15, 10, 7, 8, 5, 11,  12, 9]

# prices.sort(reverse = True)
# print(prices)

max_profit = None

# here we are seeing for each price (buy price) the maximum price
# that occurs after (sell price)
# Space complexity: O(1)
# Time complexity: O(n) - only one loop (not sure about taking max() at each iteration?)
for i in range(len(prices) - 1):
    buy_price = prices[i]
    sell_price = max(prices[i+1:])

    if (max_profit is None):
        max_profit = sell_price - buy_price
    elif((sell_price - buy_price) > max_profit):
        max_profit = (sell_price - buy_price)

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
        O(n) time - yes but unsure about running the max() function everytime?

'''
