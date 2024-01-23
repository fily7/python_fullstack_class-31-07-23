goods = (input("Введите товары через запятую: ")).split(", ")
old_index, new_index = (
    int(x) - 1 for x in (input("Позиции для перестановки: ")).split(", ")
)
goods[old_index], goods[new_index] = goods[new_index], goods[old_index]


print("Товары на полке:", ", ".join(goods))
