import math


def draw_circle(height):
    print("circle:")
    radius = math.floor(height / 2)
    for i in range(0, height):
        for j in range(0, height + 1):
            if math.sqrt(pow(i - math.floor(height / 2), 2) + pow(j - math.floor(height / 2), 2)) <= (radius + 0.5):
                print("*", end='')
            else:
                print(" ", end='')
        print()
    print()


def draw_square(height):
    print("Square:")
    for i in range(1, height + 1):
        for j in range(1, height + 1):
            print("*", end='')
        print()
    print()


def draw_right_triangle(height):
    print("Right triangle:")
    for i in range(1, height + 1):
        for j in range(1, i + 1):
            print("*", end='')
        print()
    print()


def draw_pyramid(height):
    print("Pyramid")
    for i in range(1, height + 1):
        for j in range(1, height - i + 1):
            print(" ", end='')
        for k in range(1, 2 * i):
            print("*", end='')
        print()
    print()


def sort_tuple(tup):
    lst = len(tup)
    for i in range(0, lst):
        for j in range(0, lst - i - 1):
            if tup[j][1] > tup[j + 1][1]:
                temp = tup[j]
                tup[j] = tup[j + 1]
                tup[j + 1] = temp
    return tup


shapes_list = []
shape = input("Enter the shape name (square, circle, pyramid, triangle) or enter 0 to exit: ")

while shape != "0":
    while shape != "square" and shape != "circle" and shape != "pyramid" and shape != "triangle" and shape != "0":
        shape = input("Incorrect input : Enter the shape name (square, circle, pyramid, triangle) or enter 0 to exit: ")
        if shape == "0":
            quit()

    height = input("Enter the shape's height: ")
    while int(height) <= 0:
        height = input("Please enter a positive number. Enter the shape's height: ")

    shapes_list.append((shape, int(height)))
    sorted_tuple = sort_tuple(shapes_list)

    for i in range(0, len(sorted_tuple)):
        if sorted_tuple[i][0] == "square":
            draw_square(sorted_tuple[i][1])
        elif sorted_tuple[i][0] == "circle":
            draw_circle(sorted_tuple[i][1])
        elif sorted_tuple[i][0] == "pyramid":
            draw_pyramid(sorted_tuple[i][1])
        else:
            draw_right_triangle(sorted_tuple[i][1])

    shape = input("Enter the shape name (square, circle, pyramid, triangle) or enter 0 to exit: ")

