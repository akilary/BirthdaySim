from simulation import simulate, create_birthdays


MONTHS = ("Янв", "Фев", "Мар", "Апр", "Май", "Июн",
          "Июл", "Авг", "Сен", "Окт", "Ноя", "Дек")

def main(num_birt: int) -> None:
    birthdays = create_birthdays(num_birt)

    print(f"Сгенерировано {num_birt} дней рождения:")
    print(" ".join([f"{birthday.day} {MONTHS[birthday.month - 1]}." for i, birthday in enumerate(birthdays)]))

    sim = simulate(num_birt)

    print(f"\nВероятность совпадения дней рождения среди {num_birt} человек: {sim[0]}%")
    print(f"Из 100 000 симуляций у {num_birt} человек дни рождения совпали {sim[1]} раз.")


if __name__ == '__main__':
    while True:
        num_birthday = input("Введите количество людей для генерации дней рождения:\n> ")
        try:
            num_birthday = int(num_birthday)
            main(num_birthday)
            break
        except ValueError:
            print("Некорректный ввод! Пожалуйста, введите целое число.\n")
        finally:
            input("Enter для выхода...")