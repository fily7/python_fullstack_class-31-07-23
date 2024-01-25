def calculate_discount(prices: list, sale):
    return sum(prices) * (sale / 100)


def main():
    prices = list(map(int, (input("Введите и цены и скидку: ").split(", "))))
    print("Сумма скидки:", calculate_discount(prices[:-1], prices[-1]))


if __name__ == "__main__":
    assertion = True
    if assertion:
        test1 = [100, 200, 300, 10]
        test2 = [50, 150, 250, 20]
        assert calculate_discount(test1[:-1], test1[-1]) == 60
        assert calculate_discount(test2[:-1], test2[-1]) == 90
        print("Test: OK")
    else:
        main()
