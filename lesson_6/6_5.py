prices_iter = map(int, (input("Введите цены: ")).split(", "))
prices = list(prices_iter)
max_index = prices.index(max(prices))
min_index = prices.index(min(prices))
prices[min_index], prices[max_index] = prices[max_index], prices[min_index]

print("Новые цены:", ", ".join(map(str, prices)))
