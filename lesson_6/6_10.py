prices_iter = map(int, (input("Введите цены: ")).split(", "))
prices = list(prices_iter)


print("Средняя цена товаров:", sum(prices) / len(prices))
# print("Средняя цена товаров:", sum(prices)//len(prices)) # для int
