from simulation import simulate, create_birthdays


MONTHS = ("Янв", "Фев", "Мар", "Апр", "Май", "Июн",
          "Июл", "Авг", "Сен", "Окт", "Ноя", "Дек")

def main(num_birt: int) -> None:
    """Основная функция программы для генерации дней рождения и проведения симуляций."""
    birthdays = create_birthdays(num_birt)

    print(f"\nСписок {num_birt} случайных дней рождения:")
    print(" ".join([f"{birthday.day} {MONTHS[birthday.month - 1]}." for birthday in birthdays]))

    sim = simulate(num_birt)

    print(f"\nВероятность совпадения дней рождения среди {num_birt} человек: {sim[0]}%")
    print(f"Из {sim[1]} совпадений в 100 000 симуляциях.\n")


if __name__ == '__main__':
    while True:
        num_birthday = input("Введите количество человек для генерации дней рождения:\n> ")
        try:
            num_birthday = int(num_birthday)
            main(num_birthday)
            break
        except ValueError:
            print("Ошибка: Введите целое число.\n")
        finally:
            input("Enter для выхода...")