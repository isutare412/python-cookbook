prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75,
}

# zip is a generator (cannot reuse)

min_price = min(zip(prices.values(), prices.keys()))
# min_price = min(prices.items(), key=lambda e: e[1])

max_price = max(zip(prices.values(), prices.keys()))
# max_price = max(prices.items(), key=lambda e: e[1])

prices_sorted = sorted(zip(prices.values(), prices.keys()))

print(min_price)
print(max_price)
print(prices_sorted)
