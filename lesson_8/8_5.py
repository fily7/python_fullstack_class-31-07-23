first_shop_goods = set((input("Первый магазин: ").split(", ")))
second_shop_goods = set((input("Второй магазин: ").split(", ")))


print(
    "Только в первом магазине:",
    ", ".join(first_shop_goods.difference(second_shop_goods)),
)
print(
    "Только в втором магазине:",
    ", ".join(second_shop_goods.difference(first_shop_goods)),
)
