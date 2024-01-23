goods = (input("Введите товары через запятую: ")).split(", ")
insert_index = int(input("Позиция нового товара: ")) - 1
new_good = input("Введите новый товар: ")

goods.insert(insert_index, new_good)

print("Товары на полке:", ", ".join(goods))
