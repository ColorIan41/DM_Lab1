import rectangle
import do_math
import chess
import strings


def menu():
    print("\n\nОберіть задачу:\n\n"
          "1.Обчислити площу та периметр прямокутника\n"
          "2.Обчислити середнє геометричне з двох значень\n"
          "3.Обчислити площу та периметр прямокутника у координатному просторі\n"
          "4.Перевірка числа на парність\n"
          "5.Перевірка на правильність висловлення(3 числа)\n"
          "6.Перевірка поля шахматної дошки\n"
          "7.Перевірка ходу ферзя\n"
          "8.Виведення ряду чисел\n"
          "9.Число задом наперед\n"
          "10.Операція над масивом\n"
          "11.Перевірка на просте число\n"
          "12.Обчислення функції(Варіант 22)\n"
          "13.Прізвище, імʼя, номер телефону\n"
          "14.1, 2, 3, 4, 5...\n"
          "15.Числа до 100, кратні 13\n"
          "16.Редагування рядків\n")
    t = int(input(""))
    match t:
        case 1:
            rectangle.calculate_rectangle()
            input("Press Enter to continue")
            menu()
        case 2:
            do_math.geometric_mean()
            input("Press Enter to continue")
            menu()
        case 3:
            rectangle.calculate_rectangle_xy()
            input("Press Enter to continue")
            menu()
        case 4:
            do_math.even_number_check()
            input("Press Enter to continue")
            menu()
        case 5:
            do_math.true_false()
            input("Press Enter to continue")
            menu()
        case 6:
            chess.check_chessboard()
            input("Press Enter to continue")
            menu()
        case 7:
            chess.check_queen_move_fix()
            input("Press Enter to continue")
            menu()
        case 8:
            do_math.numbers()
            input("Press Enter to continue")
            menu()
        case 9:
            do_math.reverse_number()
            input("Press Enter to continue")
            menu()
        case 10:
            do_math.work_with_array()
            input("Press Enter to continue")
            menu()
        case 11:
            do_math.prime_numbers()
            input("Press Enter to continue")
            menu()
        case 12:
            do_math.function_calculate()
            input("Press Enter to continue")
            menu()
        case 13:
            strings.fill_a_form()
            input("Press Enter to continue")
            menu()
        case 14:
            do_math.for_loop()
            input("Press Enter to continue")
            menu()
        case 15:
            do_math.thirteen()
            input("Press Enter to continue")
            menu()
        case 16:
            strings.string_redact()
            input("Press Enter to continue")
            menu()



menu()
