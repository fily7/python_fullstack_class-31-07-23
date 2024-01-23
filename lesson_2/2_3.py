books: int = int(input("Введите количество книг:"))
canc: int = int(input("Введите количество канцтоваров:"))
toys: int = int(input("Введите количество игрушек:"))

total_volume = books * 2 + canc * 1.5 + toys * 3
print(f"Общий объем: {total_volume} м^3")
