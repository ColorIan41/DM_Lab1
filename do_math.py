import statistics
import cmath
import math
import numpy


def geometric_mean():
    a = float(input("\nВведіть перше значення:\n"))
    b = float(input("Введіть друге значення:\n"))
    c = a * b
    if c >= 0:
        result = cmath.sqrt(c)
        print("Середнє геометричне -", result)
    else:
        print("Result can`t be negative so ignored. Abort")
        exit()


def even_number_check():
    try:
        a = int(input("Введіть ціле число"))
    except ValueError:
        print("Wrong value or formatting. Abort.")
        exit()
    if a % 2 == 0:
        print("Число парне")
    else:
        print("Число непарне")


def true_false():
    higher_than = bool(False)  # a < b < c
    at_least_one_positive = bool(False)
    only_one_positive = bool(False)

    try:
        a = int(input("\nВведіть a (ціле число):\n"))
        b = int(input("Введіть b (ціле число):\n"))
        c = int(input("Введіть c (ціле число):\n"))

    except ValueError:
        print("Exception occurred. Please check input data formatting")
        exit()

    arr = numpy.array([a, b, c])

    for x in arr:
        if x > 0:
            at_least_one_positive = True

    i = 0
    count = 0  # how many positive numbers
    while i < len(arr):
        count += 1
        if count == 1:
            only_one_positive = True
        i += 1

    i = 0
    current = 0  # current number
    while i < len(arr):
        if arr[i] > current:
            current = arr[i]
            higher_than = True
        else:
            higher_than = False
        i += 1

    if higher_than:
        print("\nВисловлення a < b < c є істиною")
    else:
        print("Висловлення a < b < c не є істиною")
    if at_least_one_positive:
        print("Хоча б одне з чисел є додатнім")
    else:
        print("Жодне з чисел не є додатнім")
    if only_one_positive:
        print("Тільки одне число є додатнім")


def numbers():
    try:
        a = int(input("\nВведіть перше значення (ціле число):\n"))
        b = int(input("Введіть друге значення (ціле число):\n"))

        count = 0

        if a > b:
            i = b
            while i <= a:
                print(i, end="\n")
                i += 1
                if i == a:
                    continue
                count += 1
        if b > a:
            i = a
            while i <= b:
                print(i, end="\n")
                i += 1
                if i == a:
                    continue
                count += 1
        print("Кількість чисел -", count)

    except ValueError:
        print("Exception occurred. Please check input data formatting")
        exit()


def reverse_number():
    try:
        a = int(input("\nВведіть a (ціле число, більше нуля):\n"))
        reverse = 0
        while a > 0:
            reverse = int((reverse * 10) + math.fmod(a, 10))
            a = a // 10

        print("Результат -", reverse)

    except ValueError:
        print("Exception occurred. Please check input data formatting")
        exit()


def function_calculate():
    x = -20
    y = 17.42
    z = -3.298

    a = abs(x) / (1 + 1 / math.log(y + z ** 2))

    print("Значення функції -", a)


def for_loop():
    try:
        for counter in range(4):
            number = int(input("\n"))
            if number == 5:
                print("Молодець!")
                break
            if counter == 4:
                break
    except ValueError():
        print("Exception occurred. Please check input data formatting")
        exit()


def thirteen():
    try:
        for counter in range(0, 100, 13):
            if counter % 13 == 0:
                print(counter, end="\n")

    except ValueError:
        print("Exception occurred. Please check input data formatting")
        exit()


def work_with_array():
    try:
        b = int(input("\nВведіть розмір масива (ціле число, більше нуля):\n"))
        arr = [x for x in range(0, b)]
        for y in range(0, b):
            arr[y] = int(input(f"Введіть число № {y}:\n"))

        m = statistics.median(arr)

        for z in range(0, b):
            if arr[z] >= m:
                arr[z] -= 18
        print(arr)

    except ValueError:
        print("Exception occurred. Please check input data formatting")


def prime_numbers():
    try:
        prime = bool(False)
        a = int(input("\nВведіть значення (ціле число, більше 1):\n"))
        for x in range(2, a):
            if(a % x) == 0:
                prime = False
                break
            else:
                prime = True
        if a == 2:
            prime = True

        if prime:
            print("Число є простим")
        else:
            print("Число не є простим")
    except ValueError:
        print("Exception occurred. Please check input data formatting")
        exit()


