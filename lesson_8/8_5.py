from typing import Tuple


def cross_dif(a: set, b: set) -> Tuple[set, set]:
    return a - b, b - a


def main():
    first_shop_goods = set((input("Первый магазин: ").split(", ")))
    second_shop_goods = set((input("Второй магазин: ").split(", ")))
    uniq_first, uniq_second = cross_dif(first_shop_goods, second_shop_goods)
    print("Только в первом магазине:", ", ".join(uniq_first))
    print("")
    print("Только в втором магазине:", ", ".join(uniq_second))


if __name__ == "__main__":
    assertion = True

    if assertion:
        a = set(["a", "b", "c", "d"])
        b = set(["c", "d", "e", "f"])
        ua, ub = cross_dif(a, b)
        assert ua == set(["a", "b"])
        assert ub == set(["e", "f"])
        print("test: OK")
    else:
        main()
