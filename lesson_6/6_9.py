prices_iter = map(int, (input("Введите цены: ")).split(", "))
prices = sorted(prices_iter, reverse=True)

print("Отсортированые цены:", ", ".join(map(str, prices)))
