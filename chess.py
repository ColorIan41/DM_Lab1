import numpy


def check_chessboard():
    chessboard = numpy.array([
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],  # 8x8 array(0 - white square. 1 - black space)
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0]
    ])

    square_white = bool(False)
    try:
        x = int(input("Введіть номер стовпця шахматного поля (x):"))
        y = int(input("Введіть номер ряду шахматного поля (y):"))
    except ValueError:
        print("Exception occurred. Please check input data formatting")
        exit()

    current_square = chessboard[y - 1, x - 1]

    if current_square == 0:
        square_white = True
    else:
        square_white = False

    for line in chessboard:
        print(line, end="\n")

    if square_white:
        print(f"Поле з координатою ({x}, {y}) - білого кольору")
    else:
        print(f"Поле з координатою ({x}, {y}) - чорного кольору")


def check_queen_move():
    chessboard = numpy.zeros((8, 8))

    x1 = int(input("Введіть номер стовпця шахматного поля для позиції ферзя (x1, 1-8):"))
    y1 = int(input("Введіть номер ряду шахматного поля для позиції ферзя (y1, 1-8):"))

    i = y1 - 1
    j = x1 - 1
    while 0 <= i <= len(chessboard) - 1:
        chessboard[i, j] = 1
        i += 1

    i = y1 - 1
    j = x1 - 1
    while 0 <= i <= len(chessboard) - 1:
        chessboard[i, j] = 1
        i -= 1

    i = y1 - 1
    j = x1 - 1
    while 0 <= j <= len(chessboard[0]) - 1:
        chessboard[i, j] = 1
        j += 1

    i = y1 - 1
    j = x1 - 1
    while 0 <= j <= len(chessboard[0]) - 1:
        chessboard[i, j] = 1
        j -= 1

    i = y1 - 1
    j = x1 - 1
    while 0 <= i <= len(chessboard) - 1 and 0 <= j <= len(chessboard[0]) - 1:
        chessboard[i, j] = 1
        i += 1
        j += 1

    i = y1 - 1
    j = x1 - 1
    while 0 <= i <= len(chessboard) - 1 and 0 <= j <= len(chessboard[0]) - 1:
        chessboard[i, j] = 1
        i -= 1
        j -= 1

    i = y1 - 1
    j = x1 - 1
    while 0 <= i <= len(chessboard) - 1 and 0 <= j <= len(chessboard[0]) - 1:
        chessboard[i, j] = 1
        i += 1
        j -= 1

    i = y1 - 1
    j = x1 - 1
    while 0 <= i <= len(chessboard) - 1 and 0 <= j <= len(chessboard[0]) - 1:
        chessboard[i, j] = 1
        i -= 1
        j += 1

    i = y1 - 1
    j = x1 - 1
    chessboard[i, j] = 7  # queen

    for line in chessboard:
        print(line, end="\n")

    x2 = int(input("Введіть номер стовпця шахматного поля для позиції наступного ходу (x2, 1-8):"))
    y2 = int(input("Введіть номер ряду шахматного поля для позиції наступного ходу (y2, 1-8):"))

    if chessboard[y2 - 1, x2 - 1] == 1:
        print("Такий хід можливий")
    else:
        print("Такий хід не є можливим")


def check_queen_move_fix():
    try:
        check_queen_move()
    except ValueError:
        print("Exception occurred. Please check input data formatting")
        exit()
