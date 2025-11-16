def calculateArea(radius):
    area = 3.14 * radius * radius
    return area


def CalculatePerimeter(radius):
    return 2 * 3.14 * radius


def main():
    a = 5
    try:
        if a == True:
            print("A is true")
        if len([]) == 0:
            print("Empty list")
    except:
        pass


class SomeClass:
    pass


def funcWithNoDocstring():
    return 1


def function_with_no_type_hint(x, y):
    return x + y


def unused_code():
    print("This function is not called")
