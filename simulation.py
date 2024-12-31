from datetime import date, timedelta
from random import randint


start_year = date(2001, 1, 1)


def simulate(num_birt, num_sim: int = 100000) -> tuple:
    """Проводит симуляцию совпадения дней рождения для указанного числа людей."""
    duplicate = 0
    for i in range(num_sim):
        if i % 10000 == 0:
            print(f"\rИдёт симуляция №{i} из {num_sim}...", end="")
        birthdays = create_birthdays(num_birt)
        if get_match(birthdays):
            duplicate += 1
    print("\rСимуляции завершены\n")
    return round(duplicate / 100000 * 100, 2), duplicate


def create_birthdays(num_birt: int) -> list[date]:
    """Генерирует список случайных дней рождения для заданного числа людей."""
    birthdays = []
    for i in range(num_birt):
        random_day = timedelta(randint(1, 365))
        birthdays.append(start_year + random_day)
    return birthdays


def get_match(birthdays: list[date]) -> date | None:
    """Проверяет наличие совпадающих дней рождения в списке."""
    if len(birthdays) == len(set(birthdays)):
        return None

    for a, birthday_a in enumerate(birthdays):
        for b, birthday_b in enumerate(birthdays[a + 1:]):
            if birthday_a == birthday_b:
                return birthday_a
