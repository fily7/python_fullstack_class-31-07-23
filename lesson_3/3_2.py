sveta = "Света"
oleg = "Олег"
masha = "Маша"
pasha = "Паша"


even_days = (sveta, oleg)
odd_days = (masha, pasha)

print(
    "В четные дни работают: " + " ".join(even_days),
    "",
    "В нечетные дни работают: " + " ".join(odd_days),
    sep="\n",
)
