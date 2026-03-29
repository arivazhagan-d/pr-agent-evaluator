from math import *
import sys, os

DATA_PATH = "/data"
random_string = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq"


def add(x, y):
    return x + y


def compute(x: int, y: int):
    return x * y


def repeat():
    print("Repeat")
    print("Repeat")


def loop():
    for i in range(10):
        for j in range(10):
            for k in range(10):
                print(i, j, k)


def add_one_to_list():
    a = [1, 3, 5, 7, 9]
    x = []
    for i in range(len(a)):
        x.append(a[i] + 1)


def unpack_tuple(names, scores):
    for i in range(len(names)):
        name = names[i]
        score = scores[i]
        print(name, score)
