#!/usr/bin/env python
import math
import sys
from math import factorial


def f0():
    [factorial(num) for num in [2, 4, 5, -6] if num%2 == 0]


def f1():
    with open('my_file.txt') as file:
        content = file.readlines()
        print(content)


def f2():
    count = 3
    numbers = [2, 4, 5, 6, 4.25]
    for num in numbers:
        print(num/count)
        count -= 1

def f3():
    raise FloatingPointError


def f4():
    result = math.exp(-10000)
    return result


def f5():
    count = 3
    numbers = [2, 4, 5, 6, 4.25]
    for num in numbers:
        print(num / count)
        count -= 1



def f6():
    count = 3
    numbers = [2, 4, 5, 6]
    for num in numbers:
        assert count > 0
        print(num / count)
        count -= 1



def f7():
    num_list = [2, 4, 6, 8]
    for num in num_list:
        print(num)
        num_list.delete(num)



def f8():
    with open('my_file.txt') as file:
        content = file.readlines()
        print(content)


def f9():
    import maths
    result = maths.exp(10)
    print(result)

def f10():
    names = ['John', 'Mark', 'Edward', 'Joshua']
    print(names[4])


def f11():
    stats = (('A', 0), ('B', 1), ('C', 2), ('D', 3))
    for i in range(len(stats) + 1):
        print(stats[i])



def f12():
    students = { 'Mark': 18, 'John': 22,
                 'George': 19, 'Micheal': 28
    }

    print(students['mark'])



def f13():

    def add(x, y):
        return x + y

    Add(4, 5)

                          

def f14():
    exec(" values = [8, 4, 9, 7, 0]]")
    sorted_values = sorted(values)
    print(sorted_values)



def f15():
    values = [4, 3, 2, 1, 0, -1, -2]
    for value in values:
         print(math.factorial(value))

def f16():
    with open( 'chinese.txt') as file :
        content = file.readlines()
        print(content.encode('ascii'))



def check_exception(f, exception):
    try:
        f()
    except exception:
        pass
    else:
        print("Bad luck, no exception caught: %s" % exception)
        sys.exit(1)


check_exception(f0, BaseException)
check_exception(f1, Exception)
check_exception(f2, ArithmeticError)
check_exception(f3, FloatingPointError)
check_exception(f4, OverflowError)
check_exception(f5, ZeroDivisionError)
check_exception(f6, AssertionError)
check_exception(f7, AttributeError)
check_exception(f8, EnvironmentError)
check_exception(f9, ImportError)
check_exception(f10, LookupError)
check_exception(f11, IndexError)
check_exception(f12, KeyError)
check_exception(f13, NameError)
check_exception(f14, SyntaxError)
check_exception(f15, ValueError)
check_exception(f16, UnicodeError)

print("Congratulations, you made it!")
