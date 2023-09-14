def calculate_rectangle():
    try:
        a = float(input("\nВведіть довжину:\n"))
        b = float(input("Введіть ширину:\n"))

    except ValueError:
        print("Exception occurred. Please check input data formatting")
        exit()

    s = float(a * b)
    p = float(2 * (a + b))
    if s >= 0:
        print("Площа прямокутника (s) -", s)
    else:
        print("Result can`t be negative so ignored. Abort")
        exit()
    print("Периметр прямокутника (p) -", p)
    exit()


def calculate_rectangle_xy():
    try:
        coord_x1 = int(input("\nВведіть x1:\n"))
        coord_y1 = int(input("Введіть y1:\n"))
        coord_x2 = int(input("Введіть x2:\n"))
        coord_y2 = int(input("Введіть y2:\n"))

    except ValueError:
        print("Exception occurred. Please check input data formatting")
        exit()

    if coord_x1 > coord_y1:
        a = float(coord_x1 - coord_y1)
    else:
        a = float(coord_y1 - coord_x1)

    if coord_x2 > coord_y2:
        b = float(coord_x2 - coord_y2)
    else:
        b = float(coord_y2 - coord_x2)

    s = float(a * b)
    p = float(2 * (a + b))
    print("Площа прямокутника (s) -", s)
    print("Периметр прямокутника (p) -", p)
