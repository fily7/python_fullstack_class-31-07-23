goods = (input("Введите товары через запятую: ")).split(", ")
delete_index = int(input("Позиция для удаления товара: ")) - 1

goods.pop(delete_index)

print("Товары на полке:", ", ".join(goods))
