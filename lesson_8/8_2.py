words = {
    "Красивый": "Прекрасный",
    "Уродливый": "Некрасивый",
    "Сложный": "Запутанный",
    "Простой": "Легкий",
}
for key, value in list(words.items()):
    words[value] = key


assert words["Красивый"] == "Прекрасный"
assert words["Прекрасный"] == "Красивый"

key = input("Введите слово: ")
print(f"Синоним: {words[key]}")
