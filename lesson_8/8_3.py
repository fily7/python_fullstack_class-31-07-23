goods = {"Яблоко": 100, "Банан": 80, "Кофе": 250, "Чай": 150}


cheap_one = min(goods, key=goods.get)
expensive_one = max(goods, key=goods.get)

print(f"Самый дешевый: {cheap_one} - {goods[cheap_one]} руб.")
print(f"Самый дорогой: {expensive_one} - {goods[expensive_one]} руб.")
