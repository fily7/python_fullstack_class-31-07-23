words = {
    "Красивый": "Прекрасный",
    "Уродливый": "Некрасивый",
    "Сложный": "Запутанный",
    "Простой": "Легкий",
}
for key, value in words.items():
    words[value] = key


key = input("Введите слово: ")
print(f"Синоним: {words[key]}")
