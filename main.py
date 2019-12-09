import module.flipper
import module.scrambler
import module.translator_wow
import module.translator_minlai

selectedMode = "main_menu"

while True:
    if selectedMode == "main_menu":
        print("Выберите режим работы: ")
        print("1) Переворачиватель слов")
        print("2) Скрамблер")
        print("3) Переводчик")
        choice = input("Выбор: ")
        if choice == "1":
            selectedMode = "flip_mode"
            print("Выбран режим: Переворачиватель")
            print("0) Выход")
        elif choice == "2":
            print("Выбран режим: Скрамблер")
            print("0) Выход")
            selectedMode = "scrambler_mode"
        elif choice == "3":
            print("Выбран режим: Переводчик")
            print("0) Выход")
            selectedMode = "translator_mode"
        else:
            print("Выбор неверен, можно выбрать лишь 1 или 2.")
    elif selectedMode == "flip_mode":
        print("1) Нормальный -> Перевернутый")
        print("2) Нормальный -> Перевернутый со скремблом")
        print("3) Перевернутый -> Нормальный")
        choice = input("Выбор: ")
        if choice == "1":
            module.flipper.convert_from_normal()
        elif choice == "2":
            module.flipper.convert_from_normal_and_scramble()
        elif choice == "3":
            module.flipper.convert_to_normal()
        elif choice == "0":
            selectedMode = "main_menu"
    elif selectedMode == "scrambler_mode":
        print("Доступные режимы:")
        print("1) Убить порядок букв в словах")
        print("2) Легкий, еще читаемый LEET")
        print("3) Counter-strike transLEET")
        print("4) Жесткий 31337")
        choice = input("Желаемый результат: ")
        if choice == "0":
            selectedMode = "main_menu"
        else:
            module.scrambler.scramble(choice)
    elif selectedMode == "translator_mode":
        print("Доступные режимы:")
        print("1) Русский -> Мин-Лайский Плопийский (Дневной)")
        print("2) Русский -> Мин-Лайский Плопийский (Ночной)")
        print("3) Русский -> Вовзянка")
        print("4) Русский -> Мин-Лайский Плопийский (тест)")
        choice = input("Выбор: ")
        if choice == "0":
            selectedMode = "main_menu"
        elif choice == "1":
            module.translator_minlai.translate2day()
        elif choice == "2":
            module.translator_minlai.translate2night()
        elif choice == "3":
            module.translator_wow.translate()
        elif choice == "4":
            module.translator_minlai.multitranslate()