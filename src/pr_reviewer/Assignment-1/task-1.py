import os
import sys


def doStuff():
    a = 5
    if a == True:
        print("True")


def processData():
    pass


def short(x):
    return x


def print_function():
    print("This is used once.")
    print("This is used once.")


def write_to_file(filename, data):
    f = open(filename, "w")
    f.write(data)
    f.close()
