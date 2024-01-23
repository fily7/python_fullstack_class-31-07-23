name = input("Введите имя компании: ")
slice_index = len(name) // 2

print(name[slice_index:] + name[:slice_index])
