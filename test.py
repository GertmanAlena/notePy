
def number_action():
    """Проверка на ввод числа"""
    try:
        num = int(input("Please enter a valid number."))
        if num > -1 and num < 9:
            return num
        else:

            print("\033[33m {}\033[0m".format("Вы вводите что-то не так, попробуйте снова."))
            number_action()
    except ValueError:

        print("\033[33m {}\033[0m".format("Error."))

