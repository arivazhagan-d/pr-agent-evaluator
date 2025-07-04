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


class someClass:
    pass


def add(x, y):
    return x + y


def check_none():
    a = None
    if a:
        print("a is not None")
    return None


def swap(a, b, c):
    """Swaps the values of a and b.

    Args:
        a : Input value a.
        b : Input value b.
        c : Input value c.

    Returns:
        tuple: swapped values of a and b.
    """
    temp = a
    a = b
    b = temp
    return a, b
