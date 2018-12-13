prices = [15,10, 7, 8, 5, 11,  12, 9, 7]
profits = []

for i in range(len(prices) - 1):
    buy_price = prices[i]
    max_sell_price = max(prices[i+1:])
    if (max_sell_price > buy_price):
        profits.append(max_sell_price - buy_price)

max_profit = max(profits)

print('Max profit is ' + str(max_profit))