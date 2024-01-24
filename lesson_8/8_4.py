input_str = """Снабжение, Менеджер, Иванов
Дизайн, Дизайнер, Смирнов
Снабжение, Менеджер, Петров
Дизайн, Иллюстратор, Сидоров
Маркетинг, Аналитик, Сергеев
Дизайн, Дизайнер, Васильев
"""

company_workers = dict()


for line in input_str.splitlines():
    team, duty, surname = line.split(", ")
    if team not in company_workers:
        company_workers[team] = dict()
    company_workers[team][duty] = surname


searching_teams = ["Снабжение", "Дизайн"]

# for team in company_workers:
for team in searching_teams:
    print(f"{team}:", company_workers[team])
