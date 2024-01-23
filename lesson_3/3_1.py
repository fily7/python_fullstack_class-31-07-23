products = [1, 14, 4, 8, 6, 9]


def sum(l):
    res = 0
    for i in l:
        res += i
    return res


if __name__ == "__main__":
    print(sum(products))
