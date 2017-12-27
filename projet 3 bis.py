from random import randint

labmap = \
    [[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
     [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
     [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
     [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
     [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
     [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
     [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
     [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
     [1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
     [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
     [1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]]

def show():
    line_number = 0
    column_number = 0

    for line in labmap:

        for case in line:
            print(line_number, column_number, case)
            column_number = column_number + 1
        line_number = line_number + 1
        column_number = 0

def value():
    line = int(input("line"))
    column = int(input("column"))
    print(labmap[line][column])


def random_value():
    line = randint(0, 14)
    column = randint(0, 14)
    print(line, column, labmap[line][column])


show()
while True:
    random_value()










