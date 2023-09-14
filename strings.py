def fill_a_form():
    name = input("Введіть своє імʼя :")
    surname = input("Введіть своє прізвище :")
    phone = input("Введіть свій номер телефону :")

    if name or surname or phone == True:
        print("Спасибі")
    else:
        print("Не залишайте всі поля порожніми")


def string_redact():
    c = str(input("Введіть текст:"))
    k = str(input("Введіть другий ряд тексту:"))

    a = 10 * k
    print(c, a)

    k = str(input("Введіть другий ряд тексту:"))
    print(c, k)



