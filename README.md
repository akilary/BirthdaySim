# Симуляция Парадокса Дней Рождения

*Простая консольная программа на Python для моделирования вероятности совпадения дней рождения в группе людей.*

---

## Описание

Данный проект симулирует так называемый [Парадокс Дней Рождения](https://en.wikipedia.org/wiki/Birthday_problem) -
известный парадокс теории вероятностей, заключающийся в неожиданно высокой вероятности совпадения дней рождения в
небольшой группе людей.

Программа генерирует случайные "дни рождения" в виде чисел от 1 до 365 (предполагается, что в году 365 дней и
отсутствуют високосные года), выполняет заданное количество симуляций и вычисляет вероятность того, что в группе из N
человек найдутся совпадающие даты.

---

## Запуск

### Требования

* Python 3.x
* Дополнительные библиотеки не требуются (используется только стандартная библиотека)

### Инструкция

1. Склонируйте репозиторий:

   ```bash
   git clone https://github.com/akilary/BirthdaySim.git
   ```
2. Перейдите в директорию проекта.
3. Запустите программу:

   ```bash
   python main.py
   ```
4. Следуйте инструкциям в консоли.

---

## Пример работы

```
Введите число людей в группе (для выхода введите 'q'):
> 23

Запуск симуляции...

Проведено 100000 симуляций для группы из 23 человек.
Совпадения обнаружены в 50750 случаях (50.75%).

Нажмите Enter для продолжения или 'q' для выхода...
```

---

## Особенности

* Полностью консольное приложение.
* Простая модель генерации случайных дат (1..365).
* Возможность задания любого количества людей.
* По умолчанию выполняется 100 000 симуляций для повышения точности результата.
* Обработка ошибок ввода.

---

## Структура проекта

* Вся логика реализована в одном классе `BirthdaySim`.
* Без внешних зависимостей.

---

## Лицензия

Проект распространяется под лицензией MIT. Подробнее см. [LICENSE](LICENSE).

---

## Контакты

* Автор: akilary
* Email: [a.akilary@gmail.com](mailto:a.akilary@gmail.com)
