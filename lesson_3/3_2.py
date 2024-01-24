sveta = "Света"
oleg = "Олег"
masha = "Маша"
pasha = "Паша"


workers = [sveta, masha, oleg, pasha]

print(
    "В четные дни работают: " + " ".join(workers[::2]),
    "",
    "В нечетные дни работают: " + " ".join(workers[1::2]),
    sep="\n",
)
