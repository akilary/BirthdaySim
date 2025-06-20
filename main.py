from random import randint


class BirthdaySim:
    def __init__(self, count: int):
        """
        :param count: Кол-во людей
        """
        self.people_count = count

    def run(self, total_simulations: int = 100000) -> None:
        """Запускает симуляцию"""
        print("\nЗапуск симуляции...")

        duplicate = 0
        for _ in range(total_simulations):
            birthdays = [randint(1, 365) for _ in range(self.people_count)]
            if len(birthdays) != len(set(birthdays)):
                duplicate += 1

        probability = round(duplicate / total_simulations * 100, 2)
        print(f"\nПроведено {total_simulations} симуляций для группы из {self.people_count} человек.")
        print(f"Совпадения обнаружены в {duplicate} случаях ({probability}%).")


if __name__ == "__main__":
    while True:
        try:
            user_input = input("Введите число людей в группе (для выхода введите 'q'):\n> ")
            if user_input == "q":
                break

            people_count = int(user_input)
            birthday_sim = BirthdaySim(people_count)
            birthday_sim.run()

            print("\nНажмите Enter для продолжения или 'q' для выхода...")
            if input().lower() == 'q':
                break
        except ValueError as e:
            print(f"Ошибка ввода: {e}. Пожалуйста, введите целое число.")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")
