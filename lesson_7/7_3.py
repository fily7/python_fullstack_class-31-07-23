nums = list(map(int, (input("Введите список: ")).split(", ")))

k, n, m = nums[1], nums[0], nums[-1]


print("Числа подсписка:", ", ".join(map(str, nums[n:m:k])))
